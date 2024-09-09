import tkinter as tk

class BallShooterGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Akrawat Sangkhow")
        
        
        self.canvas = tk.Canvas(root, width=500, height=500, bg="#d3d3d3")
        self.canvas.pack()
        
        
        self.ball = self.canvas.create_oval(245, 490, 255, 500, fill="blue")
        self.ring = self.canvas.create_oval(240, 50, 260, 70, outline="red", width=2)
        
        self.score,self.ball_speed,self.ring_speed,self.ring_direction = 0, 10, 5, 1
        
        self.score_label= tk.Label(root, text=f"Score:{self.score}",bg="#d3d3d3",fg="black")
        self.score_label.pack()
        
        
        self.root.bind("<space>", self.shoot_ball)
        self.move_ring()
        
    def shoot_ball(self, event):
        self.move_ball()
        
        
    def move_ball(self):
        
        ball_y = self.canvas.coords(self.ball)[1]
        if ball_y > 0:
            self.canvas.move(self.ball, 0, -self.ball_speed)
            self.root.after(50, self.move_ball if not self.check_collision() else self.update_score)
            
        else:
            self.reset_ball()
            
            
    def move_ring(self):
        self.canvas.move(self.ring, self.ring_speed * self.ring_direction, 0)
        if self.canvas.coords(self.ring)[0] <= 0 or self.canvas.coords(self.ring)[2] >= 500:
            self.ring_direction *=-1
        self.root.after(50, self.move_ring)
        
        
    def check_collision(self):
        ball_x, ball_y = self.canvas.coords(self.ball)[0], self.canvas.coords(self.ball)[1]
        ring_x1, ring_y1, ring_x2, ring_y2 = self.canvas.coords(self.ring)
        return ring_x1 < ball_x < ring_x2 and ring_y1 < ball_y < ring_y2
    
    
    def reset_ball(self):
        self.canvas.coords(self.ball, 245, 490, 255, 500)
    
    
    def update_score(self):
        self.score += 1
        self.score_label.config(text=f"Score:{self.score}:")
        if  self.score % 8 == 0:
            self.ring_speed +=2
        self.reset_ball()
        
        
root = tk.Tk()
game = BallShooterGame(root)
root.mainloop()
        
        
        