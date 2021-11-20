# Todoist Next Actions

This is a python script that allows Todoist to be able to show the "Next Actions" in each of the Projects in Todoist, a core concept in David Allen's productivity system described in his book, Getting Things Done (see summary of the system [here](https://hamberg.no/gtd/)).

https://user-images.githubusercontent.com/18186677/142727445-c2c118bf-7798-4750-896c-5a06a7f13333.mp4

## Running Locally

1. You would first need to install Python 3:

    https://www.python.org/downloads/

2. Download the repository into your PC and enter the following in the command line:
    
    ```
    cd <path>
    pip install -r requirements.txt
    ```

    Replace `<path>` with the path where you downloaded the repository.

    This should install the required libraries, such as the Todoist API.

3. Set the necessary configurations in the `config.json` (details in the **Configurations** section below). At the very least, you must set you Todoist API key.

4. Once all set, you can now run the script itself.

You can either double click on `main.py` or run it via the command line:

```
python main.py
```

## Running on a remote server

If you would rather not have the script eat up your computer's resources, you can upload the script on a remote server and have it run there.

The specifics of setting this up vary from service to service, but the simplest (and most inexpensive) method is by using a PaaS that offers a free tier.

## Configuration

There are 4 configuration values you can set.

- `API_KEY` - your Todoist API key
- `PROJECT_LABEL_TEXT` - the project label you would like to use to differentiate task items between "projects" or "tasks"
- `ACTIVE_LABEL_TEXT` - the label you would like to use to specify a task as a "next action"
- `PROCESS_ON_PROJECT_LEVEL` - by default, the script recognizes the actual Todoist Projects as the "Projects". But an alternate approach is to instread designate task items as the "Projects" by adding a project label (see above) on them.

Sample config file:

```
{
    "API_KEY": "tkzhGoo9kGcjAyNH8fPMjMx6qkDr5JXqjpQbgooD",
    "PROJECT_LABEL_TEXT": "project",
    "ACTIVE_LABEL_TEXT": "aktibo",
    "PROCESS_ON_PROJECT_LEVEL": true
}
```
