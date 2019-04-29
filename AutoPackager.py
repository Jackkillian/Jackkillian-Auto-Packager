import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mbox
from tkinter import ttk

name='JackkillianAutoPackager'

class AutoPackager():
    """Run the AutoPackager app"""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Jackkillian Auto Packager")
        self.root.geometry('750x450+0+0')
        self.def_gui()
        self.grid_gui()
        self.root.mainloop()

    def quit_app(self):
        self.quit()
        self.destroy()

    def save(self, path, save_as_entry):
        new_path = path + '/' + save_as_entry
        try:
            new_file = open(new_path, mode='w')
            new_file.write(self.main_code_input.get(1.0, tk.END))
            new_file.close()
            mbox.showinfo('Successful!', 'Saved your main code. You can close the save main code window.')
        except PermissionError:
            mbox.showerror('Permission Denied',
                           'Permission has been denied for writing to: ' + new_path + ' Please change your project path and try again.')

    def continue_no_saving(self):
        self.main_code_input.delete(1.0, tk.END)
        self.main_code_input.insert(1.0, 'Go to step 3 now')

    def continue_yes_saving(self):
        self.save_as_win = tk.Tk()
        self.save_as_entry = tk.Entry(self.save_as_win)
        self.save_as_label = tk.Label(self.save_as_win, text='Save code as:')
        self.save_as_label.grid(row=1, column=0)
        self.save_as_entry.grid(row=2, column=0)
        self.save_as_entry.insert(0, 'Must end in ".py"')
        self.save_as_button = tk.Button(self.save_as_win, text='Save', command=lambda: self.save(self.project_path.get(), self.save_as_entry.get()))
        self.save_as_button.grid(row=3, column=0)
        self.save_as_win.title('Save main code')

    def change_move_to_path(self):
        to_open = fd.askopenfilenames(initialdir='/', title='Select files to move to your project path')
        self.move_to_path.delete(0, tk.END)
        self.move_to_path.insert(0, to_open)

    def change_project_path(self):
        new_project_path = fd.askdirectory(initialdir='/', title='Select a folder for your project')
        self.project_path.delete(0, tk.END)
        self.project_path.insert(0, new_project_path)

    def move_files(self):
        try:
            files = list(self.move_to_path.get())
            for file in files:
                print(file)
                # Do this the hard way since os and shutil give me tons of errors
                old_file = open(file, mode='r')
                old_file_content = old_file.read()
                new_file = open(file, mode='w')
                new_file.write(old_file_content)
                new_file.close()
            mbox.showinfo('Files copied', 'Files have been copied to your project path!')
        except:
            mbox.showerror('Error', 'Sorry, but there was an error coping your file.'
                                    'Please just move it the normal way through you file system\nError code: 1\nError:')

    def save_setup(self, path_of_project, name, version, author, description,
                   long_description_content_type,
                   url, packages, classifiers):
        try:
            setup_file = open(path_of_project + '/setup.py', mode='w')
            setup_file.write(
                '"""Created with Jackkillian Auto Packager. To install: pip install JackkillianAutoPackager"""')
            setup_file.write('\n')
            setup_file.write('import setuptools\n')
            setup_file.write('with open("README.md", "r") as fh:\n    long_description = fh.read()\n')
            setup_file.write('\nsetuptools.setup(\n')
            setup_file.write('    name="' + name + '",\n')
            setup_file.write('    version="' + version + '",\n')
            setup_file.write('    author="' + author + '",\n')
            setup_file.write('    description="' + description + '",\n')
            setup_file.write('    long_description=long_description,\n')
            setup_file.write('    long_description_content_type="' + long_description_content_type + '",\n')
            setup_file.write('    url="' + url + '",\n')
            setup_file.write('    packages="' + packages + '",\n')
            setup_file.write('    classifiers=' + classifiers + ')\n')
            setup_file.write(
                'print("Your are now installing "+"' + name +
                '"+" packaged with Jackkillian Auto Packager. Go to github.com/Jackkillian/Jackkillian-Auto-Packager")')
            mbox.showinfo('Success!',
                        'Your setup.py has been created at: ' + path_of_project + '/setup.py' +
                        ' Now continue to the next step to publish your package!')
        except PermissionError:
            mbox.showerror('Permission Denied',
                           'Permission has been denied for writing to: ' + path_of_project + '/setup.py' + ' Please change your project path and try again.')

    def def_gui(self):
        self.label_font = ('helvetica', 20)
        self.to_save_var = tk.StringVar()
        self.steps = ttk.Notebook(self.root)
        self.step1 = tk.Frame(self.steps, bg='gray93')
        self.step2 = tk.Frame(self.steps, bg='gray93')
        self.step3 = tk.Frame(self.steps, bg='gray93')
        self.step4 = tk.Frame(self.steps, bg='gray93')
        self.step5 = tk.Frame(self.steps, bg='gray93')
        self.steps.add(self.step1, text='Step 1')
        self.steps.add(self.step2, text='Step 2')
        self.steps.add(self.step3, text='Step 3')
        self.steps.add(self.step4, text='Step 4')
        self.steps.add(self.step5, text='Step 5')
        self.move_to_path_label = tk.Label(self.step1, text='Files to move:')
        self.move_to_path = tk.Entry(self.step1)
        self.project_path_label = tk.Label(self.step1, text='Project path:')
        self.project_path = ttk.Entry(self.step1)
        self.project_path.insert(0, '/')
        self.move_to_path.insert(0, '/')
        self.change_move_to_path_button = tk.Button(self.step1, text='Change...',
                                                    command=lambda: self.change_move_to_path())
        self.change_project_path_button = tk.Button(self.step1, text='Change project path...',
                                                    command=lambda: self.change_project_path())
        self.move_files_button = tk.ttk.Button(self.step1, text='Copy files to project path',
                                               command=lambda: self.move_files())
        self.main_code_input = tk.Text(self.step2)
        self.main_code_input.insert(1.0, 'Welcome to Jackkillian Auto Packager. You can use this text box to write\ny'
                                         'our main code file for your program, or just click "Continue without saving"'
                                         '\nto go ahead to the next step.\nDon\'t forget: there\'s always help at:'
                                         '\ngithub.com/Jackkillian/Jackkillian-Auto-Packager/wiki')
        self.continue_without_saving_button = tk.ttk.Button(self.step2, text='Continue without saving',
                                                            command=lambda: self.continue_no_saving(), )
        self.divider = tk.Label(self.step1, text='', fg='gray93')
        self.warning_label = tk.Label(self.step1, text='Warning: The file copier is still in development.'
                                                       '\nYou can use it, but errors might occur.'
                                                       '\nDefinitely set the project path though.\nIt is required.')
        self.continue_with_saving_button = tk.Button(self.step2, text='Save and Continue',
                                                     command=lambda: self.continue_yes_saving())
        self.name_entry = tk.Entry(self.step3)
        self.version_entry = tk.Entry(self.step3)
        self.author_entry = tk.Entry(self.step3)
        self.description_entry = tk.Entry(self.step3)
        self.long_description_content_type_entry = tk.Entry(self.step3)
        self.url_entry = tk.Entry(self.step3)
        self.packages_entry = tk.Entry(self.step3)
        self.classifiers_entry = tk.Entry(self.step3)
        # Sorry for weird code right here, but PEP8 says the lines are too long if I don't. :-)
        self.save_setup_button = tk.Button(self.step3,
                                           text='Create setup.py',
                                           command=lambda: self.save_setup(self.project_path.get(),
                                                                           self.name_entry.get(),
                                                                           self.version_entry.get(),
                                                                           self.author_entry.get(),
                                                                           self.description_entry.get(),
                                                                           self.long_description_content_type_entry.get(),
                                                                           self.url_entry.get(),
                                                                           self.packages_entry.get(),
                                                                           self.classifiers_entry.get()
                                                                           )
                                           )
        self.command_line_label_text = """Now that you have created your setup.py, let's get your code uploaded to Pip!
        WARNING: If you used "setuptools.find_packages()" in the packages entry in the setup.py creator,
        you will need to change the file. In setuptools.setup(), in packages="setuptools.find_packages()",
        take away the quotation marks. (") You're good to go!

        NOTE: If this tutorial doesn't work, go to: https://packaging.python.org/tutorials/packaging-projects/
        
        After you have your README.md (for the long description) and the LICENSE file ready
        (for your license [For licenses, go to choosealicense.com and put the
        license text that you want into a file called LICENSE
        with no extension in your project path]), do the following:
        
        First, make sure you have the needed tools installed. Run the following commands:
        
            python3 -m pip install --user --upgrade setuptools wheel
            python3 -m pip install --user --upgrade twine

        You will also need a PyPi account. It is free. PyPi website: pypi.org
            
        Now run this command from your project path (to change path use cd ~/Path/to/project/):
        
            python3 setup.py sdist bdist_wheel
            
        Now, to upload, run the following command from your project path:
            twine upload dist/*
        You will need to input your username and password"""

        self.command_line_label = tk.Label(self.step4, text=self.command_line_label_text)
        self.congrats_label = tk.Label(self.step5, text='Congratulations! You have uploaded your package to Pip!\nWas there a bug? Please report it at: github.com/Jackkillian/Jackkillian-Auto-Packager/\nAlso, please leave your feedback at: github.com/Jackkillian/Jackkillian-Auto-Packager/\nDON\'T FORGET: Always check for updates! The next version will have a auto-running command line feature\nthat wil upload your project to Pip for you and creates a LICENSE file!')

    def grid_gui(self):
        """Grid the widgets"""
        # self.step1
        self.warning_label.grid(row=10, column=0)
        self.steps.grid(row=1, column=0)
        self.move_to_path.grid(row=2, column=0)
        self.project_path.grid(row=5, column=0)
        self.divider.grid(row=4, column=0)
        self.project_path_label.grid(row=5, column=0)
        self.move_to_path_label.grid(row=1, column=0)
        self.change_move_to_path_button.grid(row=3, column=0)
        self.change_project_path_button.grid(row=7, column=0)
        self.move_files_button.grid(row=9, column=0)
        # self.step2
        self.main_code_input.grid(row=1, column=0, columnspan=2)
        self.continue_without_saving_button.grid(row=2, column=0)
        self.continue_with_saving_button.grid(row=2, column=1)
        # self.step3
        self.name_entry.grid(row=1, column=0)
        self.version_entry.grid(row=2, column=0)
        self.author_entry.grid(row=3, column=0)
        self.description_entry.grid(row=4, column=0)
        self.long_description_content_type_entry.grid(row=5, column=0)
        self.url_entry.grid(row=6, column=0)
        self.packages_entry.grid(row=7, column=0)
        self.classifiers_entry.grid(row=8, column=0)
        # Insert for self.step3 entries
        self.name_entry.insert(0, 'Project Name e.g. AwesomePackage')
        self.version_entry.insert(0, 'Version e.g. 1.0.0')
        self.author_entry.insert(0, 'Author e.g. TheAwesomeCoder')
        self.description_entry.insert(0, 'Short Description e.g. This is an awesome package')
        self.long_description_content_type_entry.insert(0,
                                                        'Long Description Content Type e.g. text/markdown [Long description will be taken from README.md]')
        self.url_entry.insert(0, 'GitHub URL e.g. github.com/TheAwesomeCoder/AwesomePackage')
        self.packages_entry.insert(0, 'Packages e.g. setuptools.find_packages()')
        self.classifiers_entry.insert(0,
                                      'Classifiers e.g. ["Programming Language :: Python :: 3"] (must be written in list format)')
        # Grid save setup button
        self.save_setup_button.grid(row=9, column=0)
        # self.step4
        self.command_line_label.grid(row=1, column=0, columnspan=5)
        # self.step5
        self.congrats_label.grid(row=1, column=0, columnspan=5)


def main():
    app = AutoPackager()


if __name__ == '__main__':
    main()
