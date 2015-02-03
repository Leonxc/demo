### GameEntity #游戏中的实体 

Ant #蚂蚁   
预想：  
1、点击屏幕出现蚂蚁实体  
2、蚂蚁有个侦测范围X，当X范围内无leaf时，蚂蚁会随机朝一个方向走  
3、当侦测范围X内出现leaf时，ant朝leaf方向走  
!4、当侦测范围X内出现spider时，ant朝spider反方向走  
5、当3，4事件同时发生时，优先处理4  
6、ant走到leaf处会携带当前leaf一通朝蚁巢走  
7、处于6状态时，只侦测4事件  
8、ant将leaf带入蚁巢范围内，放下leaf，继续寻找leaf  
9、当spider进入蚁巢范围内时，未携带leaf蚂蚁迅速回巢驱逐spider  
10、当spider死亡后，会被ant带回蚁巢（如同leaf） 

- - -

Spider #蜘蛛   
预想：  
1、spider随机从屏幕左侧外面进入，朝一个方向走  
2、spider暂时不会攻击  
3、当spider进入蚁巢范围，ant会攻击spider，spider死亡后被带回蚁巢  
4、spider在受攻击状态增加移动速度  
5、spider走出屏幕则消失，攻击的ant恢复正常

Leaf #树叶   
预想：  
1、随机刷新在蚁巢之外  
2、被ant携带时，会跟着ant一起移动

- - -

Wrold #接受用户事件，判断用户事件，调用GameEntity实体   
预想：  
1、接受鼠标左键的点击事件，并返还点击坐标，若坐标处于蚁穴内，则出现ant   
2、监视spider走进蚁穴，进入则被未携带物品的蚂蚁攻击  
3、监视携带leaf，spider的ant是否走进蚁穴，进入则放下携带物  
4、监视spider走出屏幕，摧毁对象

- - -

State #实体所拥有的各种不同状态  
预想：  
1、

- - -

StateMachine #状态机，状态之间如何转换 

