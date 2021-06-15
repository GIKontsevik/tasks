def imposition(rec1, rec2):
    
    #Необходимо и достаточно, чтобы правый верхний угол одной фигуры
    #был не ниже или левее, чем левый нижний угол другой фигуры
    
    #Проверка левого нижнего угла одной фигуры
    if rec1[0] >= rec2[2] or rec1[1] >= rec2[3]:
        return 'false'
    
    #Проверка правого верхнего угла одной фигуры
    elif rec1[2] <= rec2[0] or rec1[3] <= rec2[1]:
        return 'false'

    else:
        return 'true'


#Или вот так я не знаю как лучше. Первый вариант чуть-чуть быстрее :/


def imposition1(rec1, rec2):
    
    #Необходимо и достаточно, чтобы правый верхний угол одной фигуры
    #был не ниже или левее, чем левый нижний угол другой фигуры.
    
    #Условия не_пересечения прямоугольников:    
    conditions = [rec1[0] >= rec2[2], rec1[1] >= rec2[3],
                  rec1[2] <= rec2[0], rec1[3] <= rec2[1]]
    
    return 'false' if any(conditions) else 'true'

rec1 = [0,0,1,1]
rec2 = [0,0,3,3]

#imposition(rec1, rec2)
#imposition1(rec1, rec2)
#get_ipython().run_line_magic('timeit', 'imposition(rec1, rec2)')
#get_ipython().run_line_magic('timeit', 'imposition1(rec1, rec2)')

