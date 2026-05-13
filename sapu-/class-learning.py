#class-learning
class SchoolReport:
    def __init__(self,student_name,math_score,jp_score,en_score): #初期化の処理
        self.student_name = student_name
        self.math_score = math_score
        self.jp_score = jp_score
        self.en_score = en_score

    def calc_avg_score(self):
        sum_score = (self.math_score+self.jp_score+self.en_score)

        avg_score = sum_score / 3
        return avg_score

sr_a = SchoolReport('田中A',100,30,50)
sr_b = SchoolReport('鈴木B',20,59,20)
sr_c = SchoolReport('斎藤C',19,22,19)

avg_a = sr_a.calc_avg_score()
avg_b = sr_b.calc_avg_score()
avg_c = sr_c.calc_avg_score()

print(sr_a.student_name)
print(sr_b.student_name)
print(sr_c.student_name)
        
print(f'田中の平均点：{avg_a}')
print(f'鈴木の平均点：{avg_b}')
print(f'斎藤の平均点：{avg_c}')
    
