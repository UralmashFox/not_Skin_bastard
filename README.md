# not_Skin_bastard I am.
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
Okay, I don't understand how to add preview picture, I will try to google it again, so, merely[![ - watch this video](//https://www.youtube.com/watch?v=AuIdL_nDsck&feature=youtu.be/maxresdefault.jpg)](https://www.youtube.com/watch?v=AuIdL_nDsck&feature=youtu.be).
And here is my pic from rviz:
![picture](https://github.com/UralmashFox/not_Skin_bastard/blob/master/Thespot.png)

