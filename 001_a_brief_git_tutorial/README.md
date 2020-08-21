# Why Version Control?

Version control software serves three important and related functions.

1) It allows you to see how your code has changed over time and, crucially, undo changes or see when errors were introduced.

2) It provides a backup and restore mechanism in case you accidentally delete a local copy of your code.

3) It allows different humans to work on the same pieces of code simultanously while minimizing the likelihood that they will murder each other.

You could only ever use git on your local machine and it would fulfill 1) just fine. If you use a cloud-hosted third party service like gitlab.com, github.com, bitbucket.com, etc, you get the benefits of 2). Most of them will also give you the benefits of 3), but will ask you for $ above some threshold of use.


# Why git?

Over the years there have been a number of popular version control systems, including CVS, SVN, Mercurial, and Git.

Git is far and away the best of these I've ever used. The key approach to git is that it captures a versioned snapshot of your entire codebase at once; it doesn't attempt to version files individually (if you've never used another VCS, great, just accept the way git does things as the way the world should work and all will be good).

# How git works

It's useful to think of git storing your files in three places. This is sort of a lie (there are more than three places your files can be), but it's a useful start.

  * A Remote Repository - this would typically be on github/gitlab/your company's internal git repo. For software that's edited by multiple individuals, this is the shared reality everyone lives in; The Truth. In order to share changes you make to the code, they need to make it back into this location (we will come back to how that happens).

  * A Local Repository - in essence this is a local mirror of the Remote Repository. You can tell git to sync your local repository with the remote repository and it will retrieve the latest version of The Truth (e.g., all the changes since the last time you checked and synced from the Remote Repository). You never edit (in a file editor sense) the local repository directly.

  * The Working Tree - this is a copy of the Local Repository that you are in the process of editing (in a file editor/software IDE sense). You are writing code in files, running it, cursing silently, etc. 

At any point while working in the Working Tree you have the option of creating a snapshot of your work. This is called a "commit". When you create a commit you tell git which files to snapshot and include a short message (called a "commit message") explaining what's up. Git saves these files back into the Local Repository in a non-destructive way; git is able to simultaneously know the last version of The Truth that it synced from the Remote Repository and the Reality As Modified By You.

Because git is tracking all these things simultaneously, it can tell you what's changed (aka "What did I break?"). The most common change you'll ask git is, "What changed between the current state of the Working Tree and my last commit to the Remote Repository?". Git will then show you all the additions and subtractions to the files you've edited since the last commit. 


