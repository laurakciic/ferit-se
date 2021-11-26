# Software Engineering Labs 2021/2022

# Author: Laura Kovačić

# Setup
- NOTE: this README.md refers mainly to my gitlab acc I work on at university

- Fork levara repo (https://gitlab.com/levara/se_labs)
- Clone your copy of the repo 
- After cloning the repo, always make sure that git knows who you are.
If you are using this repo in the labs, each time run: 

```
git config user.name "YOUR_NAME_OR_NICK"
git config user.email "YOUR_EMAIL@ADDRESS.com"
```

- Commit the README.md file to the repo with your name and push to
  origin/master
- Add user `hleventic` with a Reporter role and no expiration date
- Go to [Merlin Gitlab repozitoriji activity](https://moodle.srce.hr/2021-2022/mod/data/view.php?id=2152891) and 
  click on **Add Entry**, add the URL of the forked repo on your GitLab
  account.

# Setdown

- Commit and push everything to your repo
- Delete this directory with:

```
rm -rf /home/osirv/labs/lastname/se_labs
```

# Add additional materials to your repo

### Pulling the changes from this repo to your copy of the repo:

``` 
git remote add upstream https://gitlab.com/levara/se_labs
git fetch upstream master
git merge upstream/master
```

The first line will add the original repo as additional remote repository to your project. 
`origin` will still be your primary remote repository. This additional repository 
will be called `upstream`. 

Second line will fetch the changes from the `upstream` repo which will be saved to 
branch `upstream/master`.


Third line will merge the changes from your original repo to the `master` branch on 
your computer. All the changes should be added without conflicts or collisions.
The changes will be merged to your local repository on your computer. 

The last line will probably open the `nano` editor to change the commit message for 
the merge. If that happens exit the editor with `ctrl + X` and save the changes to the 
file ( `ctrl + x` -> `y` to save changes -> `enter` to confirm the suggested filename).

### Pushing the changes to your gitlab repo

To push the changes to your gitlab repository run:

```
git push origin master
```

After running this command all the changes imported from the original repository to 
your local copy of the repository should be visible on your project's gitlab page.

# Help, tips and tricks

[This document](README.md) will be updated with help files, tips and tricks.