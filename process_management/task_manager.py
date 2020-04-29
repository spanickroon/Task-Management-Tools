"""Process control module."""

import os
import subprocess

import psutil
import tkinter as tk
from tkinter import messagebox


class Manager:
    """Application management class."""

    def get_list_of_applications(self):
        """Receiving all snap packages and standard applications."""
        all_applications = []

        snap_packages = os.listdir(os.path.join('/snap', 'bin'))
        standard_programs = os.path.join('/usr', 'share', 'applications')

        all_applications.extend(snap_packages)

        for program in os.listdir(standard_programs):
            all_applications.append(program.replace('.desktop', ''))

        return all_applications

    def manage_application(self, app_name, close=False):
        """Starting or stopping applications and processes."""
        if close:
            for process in psutil.process_iter():
                if app_name.lower().strip() in process.name().lower():
                    process.kill()
        else:
            program = subprocess.Popen(app_name)

    def sending_messages(self, message):
        """Sending messages that are called as new windows."""
        root = tk.Tk()
        root.withdraw()
        messagebox.showwarning('New message', message.strip())


if __name__ == "__main__":
    """Testing."""
    test_manager = Manager()
    test_manager.manage_application('gnome-terminal')
    test_manager.sending_messages('hi')
