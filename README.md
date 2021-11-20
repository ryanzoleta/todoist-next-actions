# Todoist Next Actions

This is a python script that allows Todoist to be able to show the "Next Actions" in each of the Projects in Todoist, a core concept in David Allen's productivity system described in his book, [Getting Things Done](https://hamberg.no/gtd/)).

At its core, the script is very simple.

It adds an **@active** label to the topmost task of every project.

Alternatively, you can set a task as **@project**, and then the script will add **@active to** whatever is the topmost subtask in *that* task.

**Demo where Todoist Projects are treated as "Projects"**

https://user-images.githubusercontent.com/18186677/142727617-c50c4a55-ded0-4bfb-93d9-5a8af5873eb0.mp4

**Demo where Todoist Task Items are treated as "Projects"**

https://user-images.githubusercontent.com/18186677/142727622-f7de6898-504b-4043-a3c9-265f8d9dc63a.mp4

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

## Common Issues and Workarounds

- Sometimes, after making some changes to the script, then running it for the first time, an error `Item not found` is returned. I don't know the root cause for this. Somehow the script is also trying update tasks that are already archived? If you know how to solve this let me know. The easiest workaround to it is to simply run the script again.
- When the script is active, trying to reorder tasks in the Todoist app suddenly becomes clunky. Changes you make don't immediately reflect and you have to reorder them again a few times. This doesn't render the app completely useless, but it is noticeable and can get mildly annoying.

## Support

If you liked what I made please consider buying me a coffee!

[<img alt="Buy-Me-Coffee" src="https://user-images.githubusercontent.com/18186677/142728217-5ddcd972-00b7-458a-a44b-617379257e71.png" width="200">](https://www.buymeacoffee.com/ryanarnold)
