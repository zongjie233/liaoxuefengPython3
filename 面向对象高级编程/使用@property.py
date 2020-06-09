#绑定属性时，如果直接把属性暴露出去，没办法检查参数，可以在类中新建方法来设置成绩
# class Student():
#     def get_score(self):
#         return self.score
#
#     def set_score(self, score):
#         if not isinstance(score, int):
#             raise ValueError('score must be an integer!')
#         if score < 0 or score > 100:
#             raise ValueError('score must between 0~100!')
#         self.score = score
#
# h = Student()
# h.set_score(100)
# print(h.get_score())
# h.set_score(909090)#这样会抛出异常

#上述调用方式比较复杂。内置的@property可以把一个方法变成属性调用的
class Student():

    @property
    def score(self):
        return self.score_

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be an integer!')
        if score < 0 or score > 100:
            raise ValueError('score must between 0~100!')
        self.score_ = score

s = Student()
s.score = 30
print(s.score)
# s.score = 9000 #报错
