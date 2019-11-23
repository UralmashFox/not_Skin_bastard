# not_Skin_bastard I am.

[![Build Status](https://travis-ci.org/{UralmashFox}/{not_skin_bastard}.png?branch=wtf)](https://travis-ci.org/{UralmashFox}/{not_skin_bastard})

[![Build Status](https://travis-ci.org/{UralmashFox}/{not_skin_bastard}.png?branch=wtf)](https://travis-ci.com/UralmashFox/not_Skin_bastard/wtf)

Wilkommen to the best of the best ever been (no) model of robot Spot!
So, how to launch it: 
1. open your terminal on Ubuntu, which has ROS and paste this:
```
git clone https://github.com/UralmashFox/not_Skin_bastard

```
done? Good. Next:
2. paste in your terminal following:
```
source spot/devel/setup.bash
roslaunch myrobot gazebo.launch 

```
That will open Gazebo.
3. Now let's launch out controllers in another tab of terminal:
```
source spot/devel/setup.bash
roslaunch thespot_control control.launch

```
Nice, now our controllers are ready!
4. The last step. Open another one tab in the terminal and put here:
```
source spot/devel/setup.bash
rosrun thespot_python main.py

```
This magic python code makes my creation walk :3 Just impressive, my baby does it's first steps ^_^
Okay, I don't understand how to add preview picture, I will try to google it again, so, merely[![ - watch this video](//https://www.youtube.com/watch?v=AuIdL_nDsck&feature=youtu.be/maxresdefault.jpg)](https://www.youtube.com/watch?v=AuIdL_nDsck&feature=youtu.be) - there is an example of movement. Look, [![ - here](https://img.youtube.com/watch?v=PF4iUISW7YI&feature=youtu.be.jpg)](https://www.youtube.com/watch?v=PF4iUISW7YI) is video of camera working.

And here is my pic from rviz:
![picture](https://github.com/UralmashFox/not_Skin_bastard/blob/master/Thespot.png)

Some testing fun! Let's try to test my spot model. Open your terminal and do all that things upper. That will make us free from running roscore and pushing instructions when integrational test will be.
Now unit tests. Paste in the terminal:
```
source spot/devel/setup.bash
rosrun test test_FK.py

```
after this 4 files for every unit and 1 overal (not integrational) test will be. The folder is depends on your username, you can see it inthe terminal after execution.
inegrational test is running like that:
```
source spot/devel/setup.bash
rosrun test test_FKi.py

```
BUT now in another folder you have to run
```
source spot/devel/setup.bash
rosrun test FKi.py

```
in case to ged response from all the programm. The result is almostly the same as simple programm, but now it is wrapped into subscriber shell. I know, it's not very beautiful, but I tried to do my best, really :)
There is a picture of results (left - unit - tests, down right - integrational, up right - terminal with output).
![picture](https://github.com/UralmashFox/not_Skin_bastard/blob/testing/test.png)

Have a nice day!

