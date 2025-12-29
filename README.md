# Setting Up a Python Virtual Environment in IntelliJ IDEA

After cloning a Python project in **IntelliJ IDEA**, you need to create
a virtual environment (`venv`) using the terminal and then configure
IntelliJ to use it as the project's Python SDK.

------------------------------------------------------------------------

## Step 1: Clone the Repository and Open It in IntelliJ

1.  Open **IntelliJ IDEA**.
2.  On the **Welcome screen**, select **Get from VCS**
    -   Or, if a project is already open, go to **VCS → Get from Version
        Control**.
3.  Paste the repository URL and choose a local directory.
4.  Click **Clone**.
5.  When prompted, click **Trust Project**.

------------------------------------------------------------------------

## Step 2: Create the Virtual Environment

Use IntelliJ's built-in terminal to create the virtual environment.

1.  Open the **Terminal** in IntelliJ IDEA (usually at the bottom of the
    window).
2.  Run the appropriate command in the project root directory:

### macOS / Linux

``` bash
python3 -m venv venv
```

### Windows

``` bash
python -m venv venv
# or
py -m venv venv
```

This command creates a `venv` folder in the project root directory.\
Make sure `venv/` is added to your `.gitignore` file.

------------------------------------------------------------------------

## Step 3: Configure the Virtual Environment as the Project SDK

1.  Go to **File → Project Structure**
    -   Shortcut:
        -   **Windows/Linux:** `Ctrl + Alt + Shift + S`
        -   **macOS:** `Cmd + ;`
2.  In the **Project Structure** dialog, navigate to **Platform Settings
    → SDKs**.
3.  Click the **+** button and select **Add Python SDK from disk...**.
4.  Select the Python executable inside the `venv` directory:

### macOS / Linux

``` text
your_project_path/venv/bin/python
```

### Windows

``` text
your_project_path\venv\Scripts\python.exe
```

5.  Click **OK** to add the SDK.
6.  Go to **Project Settings → Project**.
7.  From the **Project SDK** dropdown, select the newly added Python
    SDK.
8.  Click **Apply**, then **OK**.

------------------------------------------------------------------------

## Step 4: Install Project Dependencies

If the repository contains a `requirements.txt` file:

1.  Open the **Terminal** in IntelliJ IDEA.
2.  Activate the virtual environment (if not already active):

### macOS / Linux

``` bash
source venv/bin/activate
```

### Windows (cmd.exe)

``` cmd
.\venv\Scripts\activate
```

3.  Install the dependencies:

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## Setup Complete

Your Python project is now configured with an isolated virtual
environment and ready to run in **IntelliJ IDEA**.
