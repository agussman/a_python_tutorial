# The Basics

To understand git, you just need to know:

 * There are infinite simultanously realities and you can travel between them;
 * You can travel through time;
 * You cannot change the past while time travelling;
 * You can create new realities from any point in time;
 * You can merge two realities, but sometimes it takes a bit of work

Pretty straight forward, right?

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

Because git is tracking all these things simultaneously, it can tell you what's changed (aka "What did I break?"). The most common change you'll ask git is, "What changed between the current state of the Working Tree and my last commit to the Remote Repository?". Git will then show you all the additions and subtractions to the files you've edited since the last commit. You can also ask git to show you all the changes between your last commit (aka "Reality As Modified By You") and your local copy of the Remote Repository (aka "The Truth").

At some point, you would may decide that Reality As Modified By You isn't that bad (you finally got that new feature to work and you can stop muttering to yourself) and you want to share it with the rest of the world/your team. In order to do that, you must reconcile ("merge") RAMBY with The Truth.

There are three ways Reality As Modified By You and The Truth can be out of sync. Two of them are fairly trivial, but one of them requires some work.

The two trivial ways are:

 * The Remote Repository has been updated but you didn't make any changes locally. This is pretty straight forward, it happens all the time. You just update your local version of the remote repository. It also means that, since you didn't change anything locally, you don't have anything you need to share back.

 * You updated your local repository, but there haven't been any intervening changes to the remote repository. Good news, you win! Your version of reality can easily become the new, shared version of reality, you just need to send it back to the remote server.

 * You changed your local repository AND the remote repository was updated. Uh oh! Now two realities are fighting for supremacy! There are two ways this can go down

   * No big deal: your realities were different in different ways (e.g., neither of you changed the same files, or similar parts of the same file ) and git just figures it out for you by combining all the changes (none of which overlap)
   * King of a big deal: you both touched the same parts of the same files. git kind of just throws up its hands and says "You're on your own!". This is called a "merge conflict". Now you have to fix it on your own. You've got two options:
     * Be a coward: If your change was small, just abandon the changes you were trying to make, switch over the latest version of the code from the remote repository, and re-implement what you were trying to do. Honestly, I do this a lot more than I'm proud to say.
     * Be a hero: Go through and sort out all the individual changes and tell git which ones to keep from each reality, or possibly sort of mash them together into a combined reality. Once you di this and give it a thumbs up, git is able to proceed from there. Most IDEs have tooling to help you do this so it's not completely backbreaking.


# git commands

## Create or getting a git remository

Create a new local repository:
```
git init
```

or

Check out a remote repository:
```
git clone <connection string to remote repo>
```

## Saving your changes

Capture the alternate relating you've been working on in your Working Tree with:

```
git add <filepath>
```

`filepath` can be one or more individual files, a directory, a new file, etc

Travel forward in time for your current reality and create a commit:
```
git commit -m "Useful message explaining what I've done"
```

# Sharing your changes with everyone else

First, update your local copy of the Remote Repository
```
git fetch <optional branch name>
```

Merge the latest version of The Truth into your version of reality
```
git merge <branch name>
```

The above two steps can be combined into the single command:
```
git pull
```

Share your changes back with the rest of the world:
```
git push
```

