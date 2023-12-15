import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext  # scrolledtext 모듈 추가
from tkcalendar import DateEntry
from datetime import datetime, timedelta

class ScheduleApp:
    def __init__(self, master):
        self.master = master
        self.master.title("팀 일정 관리")

        self.meeting_start_date = None
        self.meeting_end_date = None
        self.team_schedules = {}
        self.added_times = set()

        tk.Label(self.master, text="회의 시작 날짜").grid(row=0, column=0)
        tk.Label(self.master, text="회의 끝 날짜").grid(row=0, column=1)

        self.meeting_start_date_entry = DateEntry(self.master, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern="y-mm-dd")
        self.meeting_start_date_entry.grid(row=1, column=0)

        self.meeting_end_date_entry = DateEntry(self.master, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern="y-mm-dd")
        self.meeting_end_date_entry.grid(row=1, column=1)

        tk.Button(self.master, text="회의 날짜 설정", command=self.set_meeting_dates).grid(row=3, column=0, columnspan=2)
        tk.Label(self.master, text="--- 회의 불가능 한 날을 추가 하기 전에 '회의 날짜'를 '먼저' 설정하세요 ---").grid(row=4, column=0, columnspan=2)

        tk.Label(self.master, text="날짜").grid(row=5, column=0)
        tk.Label(self.master, text="시작 시간").grid(row=5, column=1)
        tk.Label(self.master, text="끝 시간").grid(row=5, column=2)

        self.date_entry = DateEntry(self.master, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern="y-mm-dd")
        self.date_entry.grid(row=6, column=0)

        self.start_time_entries = []
        self.end_time_entries = []
        self.add_time_entry()

        tk.Button(self.master, text="일정 추가", command=self.add_schedule).grid(row=7, column=0, columnspan=3)
        tk.Button(self.master, text="겹치지 않는 일정 보기", command=self.find_non_overlapping_schedules).grid(row=8, column=0, columnspan=3)
        tk.Button(self.master, text="겹치지 않는 시간대 보기", command=self.show_non_overlapping_time_slots).grid(row=9, column=0, columnspan=3)

    def set_meeting_dates(self):
        self.meeting_start_date = self.meeting_start_date_entry.get_date()
        self.meeting_end_date = self.meeting_end_date_entry.get_date()
        messagebox.showinfo("알림", f"회의 날짜가 설정되었습니다.\n시작 날짜: {self.meeting_start_date}\n끝 날짜: {self.meeting_end_date}")

    def add_schedule(self):
        if not (self.meeting_start_date and self.meeting_end_date):
            messagebox.showwarning("경고", "회의 날짜를 먼저 설정하세요.")
            return

        schedule_date = self.date_entry.get_date()

        if self.meeting_start_date <= schedule_date <= self.meeting_end_date:
            start_times = [entry.get() for entry in self.start_time_entries]
            end_times = [entry.get() for entry in self.end_time_entries]

            if all([schedule_date] + start_times + end_times):
                for start_time, end_time in zip(start_times, end_times):
                    try:
                        start_time_obj = datetime.strptime(start_time, "%H:%M")
                        end_time_obj = datetime.strptime(end_time, "%H:%M")

                        if start_time_obj < end_time_obj:
                            schedule = {
                                "날짜": schedule_date,
                                "시작 시간": start_time,
                                "끝 시간": end_time
                            }
                            self.team_schedules.setdefault(schedule_date, []).append(schedule)
                            self.added_times.add((schedule_date, start_time, end_time))
                        else:
                            messagebox.showerror("에러", "시작 시간이 끝 시간보다 빠를 수 없습니다.")
                            return
                    except ValueError:
                        messagebox.showerror("에러", "시작 시간과 끝 시간을 HH:MM 형식으로 입력하세요.")
                        return

                messagebox.showinfo("성공", "일정이 추가되었습니다.")
                self.clear_entries()
            else:
                messagebox.showerror("에러", "모든 필드를 입력하세요.")
        else:
            messagebox.showerror("에러", "일정 날짜가 회의 날짜 범위를 벗어납니다.")

    def find_non_overlapping_schedules(self):
        non_overlapping_schedules = self.get_non_overlapping_schedules()

        if non_overlapping_schedules:
            non_overlapping_schedules_within_meeting = []
            for schedule in non_overlapping_schedules:
                if self.meeting_start_date <= schedule["날짜"] <= self.meeting_end_date:
                    non_overlapping_schedules_within_meeting.append(schedule)

            meeting_period = set([self.meeting_start_date + timedelta(days=i) for i in range((self.meeting_end_date - self.meeting_start_date).days + 1)])
            remaining_dates = sorted([date for date in meeting_period if date not in set(self.team_schedules.keys())])

            schedule_text = "\n".join([f"{date.strftime('%Y-%m-%d (%a)')}" for date in remaining_dates])

            if self.added_times:
                added_times_text = "\n".join([f"{date.strftime('%Y-%m-%d (%a)')} {start_time} ~ {end_time}" for date, start_time, end_time in sorted(self.added_times)])
                self.display_result("겹치지 않는 일정", f"{schedule_text}\n\n--- 시간 불가능한 날짜 ---\n{added_times_text}")
            else:
                self.display_result("겹치지 않는 일정", schedule_text)
        else:
            messagebox.showinfo("알림", "겹치지 않는 일정이 없습니다.")

    def get_non_overlapping_schedules(self):
        non_overlapping_schedules = []

        for schedules in self.team_schedules.values():
            for schedule in schedules:
                is_overlapping = False

                for other_schedules in self.team_schedules.values():
                    for other_schedule in other_schedules:
                        if schedule["날짜"] == other_schedule["날짜"] and schedule != other_schedule:
                            if (schedule["시작 시간"] <= other_schedule["끝 시간"]) and (schedule["끝 시간"] >= other_schedule["시작 시간"]):
                                is_overlapping = True
                                break

                if not is_overlapping:
                    non_overlapping_schedules.append(schedule)

        return non_overlapping_schedules

    def show_non_overlapping_time_slots(self):
        if not (self.meeting_start_date and self.meeting_end_date):
            messagebox.showwarning("경고", "회의 날짜를 먼저 설정하세요.")
            return

        non_overlapping_time_slots = self.get_non_overlapping_time_slots(self.meeting_start_date, self.meeting_end_date)

        if non_overlapping_time_slots:
            formatted_time_slots = "\n".join(non_overlapping_time_slots)
            self.display_result("겹치지 않는 시간대", formatted_time_slots)
        else:
            messagebox.showinfo("알림", "겹치지 않는 시간대가 없습니다.")

    def get_non_overlapping_time_slots(self, start_date, end_date):
        all_scheduled_time_slots = set()

        for date in self.team_schedules.keys():
            if start_date <= date <= end_date:
                for schedule in self.team_schedules[date]:
                    start_time_obj = datetime.strptime(schedule["시작 시간"], "%H:%M")
                    end_time_obj = datetime.strptime(schedule["끝 시간"], "%H:%M")
                    all_scheduled_time_slots.add((date, start_time_obj, end_time_obj))

        available_time_slots = set()

        for date in self.get_date_range(start_date, end_date):
            for hour in range(24):
                current_time = datetime(year=date.year, month=date.month, day=date.day, hour=hour, minute=0)
                end_time = current_time + timedelta(hours=1)
                if all((current_time, end_time)) not in all_scheduled_time_slots:
                    available_time_slots.add((date, current_time, end_time))

        for date, start_time, end_time in sorted(all_scheduled_time_slots):
            if start_date <= date <= end_date:
                for hour in range(start_time.hour, end_time.hour):
                    current_time = datetime(year=date.year, month=date.month, day=date.day, hour=hour, minute=0)
                    end_time = current_time + timedelta(hours=1)
                    available_time_slots.discard((date, current_time, end_time))

        formatted_time_slots = []

        for date, start_time, end_time in sorted(available_time_slots):
            formatted_time = f"{date.strftime('%Y-%m-%d (%a)')} {start_time.strftime('%H:%M')} ~ {end_time.strftime('%H:%M')}"
            formatted_time_slots.append(formatted_time)

        return formatted_time_slots

    def get_date_range(self, start_date, end_date):
        date_range = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]
        return date_range

    def display_result(self, title, content):
        result_window = tk.Toplevel(self.master)
        result_window.title(title)

        text_area = scrolledtext.ScrolledText(result_window, width=40, height=20, wrap=tk.WORD)
        text_area.insert(tk.INSERT, content)
        text_area.config(state='disabled')
        text_area.pack(expand=True, fill='both')

    def clear_entries(self):
        self.date_entry.delete(0, tk.END)

        for start_entry, end_entry in zip(self.start_time_entries, self.end_time_entries):
            start_entry.destroy()
            end_entry.destroy()

        self.start_time_entries.clear()
        self.end_time_entries.clear()
        self.add_time_entry()

    def add_time_entry(self):
        start_time_combobox = ttk.Combobox(self.master, values=self.get_time_list().copy(), width=8)
        start_time_combobox.grid(row=6, column=1 + len(self.start_time_entries) * 2)
        self.start_time_entries.append(start_time_combobox)

        end_time_combobox = ttk.Combobox(self.master, values=self.get_time_list().copy(), width=8)
        end_time_combobox.grid(row=6, column=2 + len(self.end_time_entries) * 2)
        self.end_time_entries.append(end_time_combobox)

    def get_time_list(self):
        return [f"{hour:02d}:{minute:02d}" for hour in range(0, 24) for minute in range(0, 60, 60)]

if __name__ == "__main__":
    root = tk.Tk()
    app = ScheduleApp(root)
    root.mainloop()