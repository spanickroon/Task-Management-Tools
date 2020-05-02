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
            all_applications.append(
                program.replace(
                    '.desktop', '').replace('org.gnome.', 'gnome-').lower())

        return ','.join(all_applications)

    def manage_application(self, app_name, close=False):
        """Starting or stopping applications and processes."""
        try:
            if close:
                for process in psutil.process_iter():
                    if app_name.lower().strip() in process.name().lower():
                        process.kill()
            else:
                program = subprocess.Popen(app_name)
        except FileNotFoundError:
            pass

    def sending_messages(self, message):
        """Sending messages that are called as new windows."""
        root = tk.Tk()
        root.withdraw()
        messagebox.showwarning('New message', message.strip())
