# Hacker Mode

>An Easy To Use, Very Cool Looking Hacker-esque Program

This repo is intended to be used via an alias, from anywhere in your file system, to be quickly and easily make you look like a hacker.

## How To Use

### Use Cases

- Boss walks behind you
- Anyone else walks behind you
- Want to impress your friends
- Want to feel smart whilst fighting a losing battle to a complex (or maybe simple) bug

### Command: `hackermode`

> gives the appearance that you are typing a whole lot more than you actually are.

This command will print out a random length line of randomly sorted **cool** characters on every keystroke. You can add more cool characters in `hacklib.py`.

To exit the command, simply hit the 'q' key on your keyboard.

This command is pretty glitchy, if you run it for too long then it will likely start to slow down your computer. Also, on my machine, it prints out all of the typed characters when exited. Any fixed would be appreciated, I just don't have to time to get this cleaned up.

### Command: `autohackermode`

>Less glitchy, also less cool.

Clears the screen and then automatically prints a random length string of random **cool** characters on random intervals between 0 and 1 seconds.

There is no exit key on this one, you just have to force stop the program using `^C` or some other method.

## How To Setup

### Step 1: Get the Python Files to Run

```bash
# Clone this repository
$ git clone https://github.com/thetravisweber/hackermode.git

# Change Directory into the newly cloned repository
$ cd hackermode

# Run the file!
$ python3 hackermode.py
```

### Step 2: Make Alias

> This step is important so that you can quickly look like a hacker when someone walks up behind you.

Edit your terminal configuration profile so that hackermode.py and autohackermode.py can be called from anywhere in your system

```bash
# Open up your Profile 
$ nano ~/.bash_profile 
# Note: your terminal configuration file may have a different name
```

Inside of the Configuration File, insert the following lines, but swap in the path to where you have stored this repo

```bash
alias hackermode='python3 ~/path/to/this/repository/hackermode/hackermode.py'
alias autohackermode='python3 ~/path/to/this/repository/hackermode/autohackermode.py'
```

### Step 3: Reload the Terminal Configuration File

This can also be done by quitting and re-opening terminal

```bash
$ source ~/.bash_profile
# Note again: your terminal configuration file may have a different name
```

## Contributing

### TodoList

- Make all output text green (my terminal text is always green which is why I have not bothered with this yet)
- Fix glitches in `hackermode` command
