Mac/Linux
=========

Your Mac comes with an application called Terminal, which you can open from
Spotlight or your Applications folder. Another popular terminal for macOS that
you can install is [iTerm2](https://www.iterm2.com/). On Ubuntu a similar
application is available from the launcher. The terminal gives you access to
a Unix shell in which you can use a 
[variety of commands](http://mally.stanford.edu/~sr/computing/basic-unix.html) 
for interacting with your computer and running programs. You can change 
directories with `cd` and list files with `ls`, which will be familiar if you 
took CS50 in the past.

In addition to using a terminal, you will also need a text editor to work on 
your programs locally. Popular choices include 
[Sublime Text](https://www.sublimetext.com/) and [Atom](https://atom.io/), 
which you can download and install on your machine. If you are feeling more 
adventurous, consider exploring [Vim](http://www.vim.org/) or 
[Emacs](https://www.gnu.org/software/emacs/), both of which have steeper 
learning curves but can lead to potentially higher productivity. Making sure 
that _syntax highlighting_ is turned on in your editor will help make your 
code-writing experience smoother.

While you will write code in a text editor, you will likely test and run your 
programs in a terminal. For testing, it is especially helpful to be familiar 
with [I/O redirection](http://linuxcommand.org/lc3_lts0070.php). You can use 
the `>` symbol to redirect standard output of a program to a file. For 
instance, running `wc foo.txt > bar.txt` will count the number of lines, 
words, and characters in `foo.txt` and write those values into a file called 
bar.txt, either by making a new file or overwriting one if it already exists. 
Using `>>` instead would append the output of a program to the specified file. 
Redirecting output is useful for recording many outputs and then being able to 
refer to them later. Standard input can also be redirected such that a program 
would read from a file instead of taking input from the keyboard. With this, 
you could programmatically generate test cases in a text file and redirect 
the input of a program to read from that file using the `<` symbol. Pipes are 
another useful technique that allow you to use the output of one program as 
the input of another program, and they are written using the `|` symbol. Check
out [this Piazza post](https://piazza.com/class/jcnb12ohn9d5le?cid=336) for an
example of how to use this.

For GOBOSORT, if you had test data in the specified format in the file 
`test_data.txt` and wanted to feed it to your python program `submission.py` 
as input, you would run `cat test_data.txt | python submission.py`. The 
command `cat` prints out the contents of a file to stdout, and the pipe 
operator redirects this as input to your Python script.

There is plenty more that can be said about the terminal and text editors and 
indeed entire books have been written on the subject. We encourage you to 
build comfort with these tools as they will be essential beyond this class.
