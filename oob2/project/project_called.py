from condo import Condo

ideo = Condo("ideo5",18,"Ladphrao",80,"Condo 20 Floors")
ideo.show()

from project import Project

home = Project("Ladawan",15,"BangYai")
home.show()
home.update_budget(30)
print(f'budget : {home.get_budget()} MB')