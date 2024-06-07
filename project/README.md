# Final Project

## Foreword

Over this course, you've embarked on an enriching journey into the world of database application development, utilizing the Django framework. You've brushed up on your Python programming. You've learned or relearned SQL and non-SQL database syntax and semantics, transformed data across different text-based database formats, and written queries to filter, sort, and summarize data. Additionally, you've explored Django’s Object-Relational Mapping (ORM) and worked with everything from static templates to dynamic web forms.

Now, it's time to apply these skills in a practical, real-world context through your final course project. This is not just an opportunity to consolidate your knowledge, but also a platform to showcase your creativity and problem-solving abilities.

In this project, you will design and implement a comprehensive database application that encapsulates all the concepts and skills you've acquired throughout the course. This project will serve as a testament to your ability to effectively use and understand these concepts in the development of a complex, fully-functional web application.

As you undertake this project, view challenges as opportunities for growth and learning. Remember, every problem you encounter is a chance to deepen your understanding and improve your skills. Your determination, resilience, and resourcefulness will be your most valuable assets during this project—and in your future endeavors. I am confident that you will rise to the occasion and demonstrate the depth of your capabilities through this project. I eagerly anticipate your innovative and dynamic applications!

Happy coding,

Sean

## Overview

Your task is to develop a web-based, database application that fulfills the requirements listed below. You may use any of the tools and techniques we've covered in this course. When complete, there are two important components to the project submission:

- **_Live project:_** Provide me with access to the live project, running on the Internet, **until 3 days after the final day of course finals**. After this date, you may remove my access and/or decommission the site. I need to be able to login as the _admin_ user and as a _sean_ user to test your permissions. (See requirements below.)

- **_Project submission:_** Submit your project as a bundle.docx file containing your project folder to the Assignment in Canvas by the due date. Due to its final placement in the course schedule, **the project cannot be submitted late.** If you're building your project directly on PythonAnywhere, you can run this command in the Bash shell to create a zip file of your entire project folder that you can download for bundling:

```bash
zip -r project.zip ./*
```

Then go to the Files section of the PythonAnywhere dashboard to download the zip file. Extract it to your local computer, and then, as per usual...

Bundle your project folder into a `bundle.docx` file by simply placing [`bundle`](https://github.com/seansbox/pybundler/raw/main/bundle.exe) in your project folder and running it. The required files, such as \*.py, Pipfile, screenshot.jpg, etc., will be automatically included. Finally, submit the `bundle.docx` file to _Canvas_.

## Requirements

This project, which represents approximately 10% of your total course grade, will be assessed based on the following components (100 points in total):

| Description                                                                                                                                                                            | Points | Partial | Incomplete |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ------- | ---------- |
| Developed using the Django framework and deployed to PythonAnywhere.                                                                                                                   | 10     | 8       | 5          |
| Includes a minimum of 2+ models, interconnected with appropriate and meaningful referential relationships and integrity (OneToOne, ForeignKey, etc.).                                  | 15     | 12      | 8          |
| Provides a superuser account with access to an administrative interface which includes streamlined data interactions (e.g. field groups, inline forms, etc.) (Creds: admin/adminadmin) | 10     | 8       | 5          |
| Provides a sample user account with access to only certain view/model permissions as appropriate (e.g. can read but not update/delete, etc.) (Creds: sean/seansean!)                   | 10     | 8       | 5          |
| Provides adequately secured pages (driven by templates and views) for all database actions (full CRUD), and includes a public homepage.                                                | 15     | 12      | 8          |
| Has a straight-forward navigation and a consistent look-and-feel. UI elements provide access to only the appropriate pages.                                                            | 15     | 12      | 8          |
| Includes one or more unique and/or customized static files.                                                                                                                            | 10     | 8       | 5          |
| Includes one or more third-party Python packages which enhance the site's functionality or user experience.                                                                            | 15     | 12      | 8          |

Remember that these are minimum requirements. You are encouraged to exceed these requirements and demonstrate creativity and innovative thinking in your final project.

Please note that your final project will be evaluated based on adherence to these requirements, code quality, functionality, usability, aesthetics, and the complexity of implemented features. Plan your project carefully, and manage your time effectively to meet the submission deadline.
