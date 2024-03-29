# BSM Robotics MyWork
## Remote work tracking without the hassle

### Before you begin
You'll need a github account (github.com). _Use your school email address._

Once you've signed up for github, your teacher will need to invite into the MyWork repository, so talk to them about this.

### The very first time you ever use MyWork
#### If the pi has a `my_work` folder (at `/home/student/my_work`)
Enter the `my_work` folder and run `bash create_my_folder flast00` where flast00 is your BSM email prefix. Github will ask you to log in.

#### If the pi does not have a `my_work` folder
Enter the home folder for the student user (`/home/student/`) and run `git clone -b master --single-branch https://github.com/bsmrobotics/my_work.git`. Then run `bash create_my_folder flast00`

### Working with MyWork
After you've run the `create_my_folder` command, you can just work in the `my_work` directory and save your work as usual. Make directories, create files, save files, run robots, etc.

### Saving your work to the cloud
# You must save your work like this every time or you will 99% certainly lose everything you've done!
Make sure you're in `my_work` and run `bash save_my_work flast00`. Github will ask you to log in.

### Loading your work from the cloud
Make sure you're in `my_work` and run `bash load_my_work flast00`. Github will ask you to log in.

### If things go wrong...
1. Copy the recovery script to the parent directory of `my_work`. I.e., the parent directory is the directory that contains `my_work`. 
1. Go to the parent directory of `my_work`. If you're in `my_work` you can do this with `cd ..`.
1. Run the recovery script with `bash recover_from_error flast00`.
1. Go back into `my_work` with `cd my_work` and keep going. Don't forget to save your work!
