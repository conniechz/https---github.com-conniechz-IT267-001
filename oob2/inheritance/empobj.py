from empit import EmpIT
from empmkt import EmpMKT

mike = EmpIT("001","Mike",60000)
mike.add_skill("Python , JavaScript")
mike.add_experience(5)
mike.emp_detail()
mike.it_salary()

anna = EmpMKT("002","Anna",3000)
anna.emp_detail()
anna.mkt_salary()

paul = EmpMKT("003","Paul",45000)
paul.add_commision(35)
paul.add_location("Chiang Mai")
paul.emp_detail()
paul.mkt_salary()