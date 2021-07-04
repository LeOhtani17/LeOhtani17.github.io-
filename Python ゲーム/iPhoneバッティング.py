from scene import *
from time import sleep
import random
import sound
import ui

no_hit_judge=['満塁で見逃し三振','二者残塁で見逃し三振','一者残塁で見逃し三振','走者無しで見逃し三振','死球','四球']
no_hit_rank=[20,18,16,14,9,8]
swing_judge=['満塁で空振り三振','二者残塁で空振り三振','一者残塁で空振り三振','走者無しで空振り三振','振り逃げで出塁']
swing_rank=[19,17,15,13,11]
hit_judge=['ファインプレーでアウト','エラーで出塁','ヒット','ツーベースヒット','スリーベースヒット','ソロホームラン','ツーランホームラン','スリーランホームラン','満塁ホームラン']
hit_rank=[12,10,7,6,5,4,3,2,1]
mngs=5
krbr=4
hitt=8
class Intruction(Scene):
	def setup(self):
		global count,c,hit,drive_x,drive_y,minogashi,karaburi,hitto
		
		minogashi=random.randint(0,mngs)
		karaburi=random.randint(0,krbr)
		hitto=random.randint(0,hitt)
		sound.play_effect(name='bgm_maoudamashii_8bit18.mp3',volume=1,looping=True)
		count=1
		c=0
		hit=0
		self.batter=SpriteNode('アートボード 1@4x.png',position=(205,450))
		self.batter.z_position=-1
		self.batter.size=(414,896)
		self.add_child(self.batter)
		self.x = 130
		self.y = 10000
		
		self.ball = SpriteNode('pzl:BallGray', position=(self.x, self.y))
		self.ball_hit=SpriteNode(Texture('pzl:BallGray'))
		self.add_child(self.ball_hit)
		self.ball_x=0
		self.ball_y=0
		self.y_speed = -3
		self.ball_size = 0.35
		self.drive_x=random.randint(-4,4)
		self.drive_y=random.randint(3,8)
		self.ohtani=SpriteNode(Texture('構え1.png'), position=(310,450))
		self.add_child(self.ohtani)
		self.ichiro=SpriteNode(Texture('投球1.png'), position=(150,645))
		self.add_child(self.ichiro)
	def touch_began(self,touch):
		global count,c
		self.ichiro.texture=Texture('投球2.png')
		count=1000
		self.x = 150
		self.y = 700
		self.ball_x=0
		self.ball_y=0
		self.ball.size = (self.ball_x,self.ball_y)
		self.add_child(self.ball)
	def touch_ended(self,touch):
		global c,count
		self.ohtani.texture=Texture('打撃3.png')
		c=1000
		count=10000

	def update(self):
		global count,c,hit
		count+=1
		c+=1
		if c==9:
			self.ohtani.texture=Texture('構え2.png')
		if c==18:
			self.ohtani.texture=Texture('構え3.png')
		if c==27:
			self.ohtani.texture=Texture('構え4.png')
		if c==36:
			self.ohtani.texture=Texture('構え5.png')
		if c==45:
			c=9
		if count==1010:
			self.ichiro.texture=Texture('投球３.png')
		if count==1030:
			self.ichiro.texture=Texture('投球4.png')
		if count==1060:
			self.ichiro.texture=Texture('投球5.png')
			self.ohtani.texture=Texture('打撃1.png')
			c=46
		if count==1070:
			self.ichiro.texture=Texture('投球6.png')
			self.ohtani.texture=Texture('打撃2.png')
		if count==1080:
			self.ichiro.texture=Texture('投球7.png')
		if count==1090:
			self.ichiro.texture=Texture('投球8.png')
		if count==1100:
			self.ichiro.texture=Texture('投球9.png')
		if count==1110:
			self.ichiro.texture=Texture('投球10.png')
		if count==1120:
			self.ichiro.texture=Texture('投球11.png')
		if count==1130:
			sound.play_effect('se_swing1.mp3')
		if count>=1130:
			self.ichiro.texture=Texture('投球12.png')
			self.y += self.y_speed
			self.ball_x +=self.ball_size
			self.ball_y +=self.ball_size
			self.ball.size = (5+self.ball_x,5+self.ball_y)
			self.ball.position = (self.x, self.y)
		if self.ball.size >=(35,35):
			self.ball_size=0
		if count==1140:
			self.ichiro.texture=Texture('投球13.png')
		if count>=1150:
			self.ichiro.texture=Texture('投球14.png')
			self.y += -1.5
			self.ball.position = (self.x, self.y)
		if count==1400:
			sound.stop_all_effects()
			font=('Futura',25)
			LabelNode(text=no_hit_judge.pop(minogashi),font=font,parent=self,position=(205,825),color='white')
		if c==1005:
			self.ohtani.texture=Texture('打撃4.png')
		if c==1010:
			self.ohtani.texture=Texture('打撃5.png')
		if c==1015:
			self.ohtani.z_position=-100
			self.ohtani=SpriteNode(Texture('打撃6.png'), position=(265,420))
			self.add_child(self.ohtani)
		if c==1020:
			self.ohtani.z_position=-100
			self.ohtani=SpriteNode(Texture('打撃7.png'), position=(290,420))
			self.add_child(self.ohtani)
			self.collision=SpriteNode(Texture('iob:minus_circled_256'),position=(150,435))
			self.collision.size=(15,15)
			self.collision.z_position=-100
			self.add_child(self.collision)
			if abs(self.ball.position.y-self.collision.position.y)<17:
				hit=1
				sound.play_effect('野球・金属バット・打撃03_1.mp3')
				self.x_hit=self.x
				self.y_hit=self.y
				self.ball_hit_size=self.ball_x
		if hit==1:
			self.ball.z_position=-100
			self.ball_hit.z_position=-1
			self.ball_hit.position = (self.x_hit, self.y_hit)
			self.ball_hit_size-=random.uniform(0.1,0.5)
			self.x_hit+=self.drive_x
			self.y_hit+=self.drive_y	
			self.ball_hit.size=(self.ball_hit_size,self.ball_hit_size)
		if self.ball_hit.size<=(0,0):
			self.ball_hit.z_position=-100
			
		if c==1025:
			self.collision.z_position=-50
			self.ohtani.z_position=-100
			self.ohtani=SpriteNode(Texture('打撃8.png'), position=(360,410))
			self.add_child(self.ohtani)
		if c==1030 and hit==1:
			self.ohtani.z_position=-100
			self.ohtani=SpriteNode(Texture('打撃9.png'),position=(350,470))
			self.add_child(self.ohtani)
		if c==1030 and hit==0:
			self.ohtani.z_position=-100
			self.ohtani=SpriteNode(Texture('空振り1.png'),position=(335,490))
			self.add_child(self.ohtani)
		if c==1035 and hit==1:
			self.ohtani.z_position=-100
			self.ohtani=SpriteNode(Texture('打撃10.png'),position=(250,400))
			self.add_child(self.ohtani)
			font=('Futura',25)
			LabelNode(text=hit_judge.pop(hitto),font=font,parent=self,position=(205,825),color='white')
		if count>1400 and c==1035 and hit==0:
			self.ohtani.z_position=-100
			self.ohtani=SpriteNode(Texture('空振り2.png'),position=(255,405))
			self.add_child(self.ohtani)
			font=('Futura',25)
			LabelNode(text=swing_judge[karaburi],font=font,parent=self,position=(205,825),color='white')
			print(swing_rank[karaburi])
			swing_judge.pop(karaburi)
		if c==1200:
			sound.stop_all_effects()
			
			v = ui.View()
			v.background_color = 'Black'
			text = ui.TextField()
			text.size=(200,32)
			text.placeholder='次のプレイヤーの名前を入力'
			text.name = 'label'
			text.autoresizing='w'
			button=ui.Button(title='次へ')
			button.center = (v.width * 0.5, v.height * 0.7)
			button.size=(50,50)
			button.flex = 'LRTB'
			button.action=nextgame
			v.add_subview(button)
			v.add_subview(text)
			v.present('sheet1')
			
def howmanyplayers(sender):
	kazu=sender.superview['プレイ人数'].text
	run(Intruction())
def nextgame(self):
	run(Intruction())
	
v=ui.load_view()

v.present('sheet')
