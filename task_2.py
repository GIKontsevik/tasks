#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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


# In[ ]:


def imposition1(rec1, rec2):
    
    #Необходимо и достаточно, чтобы правый верхний угол одной фигуры
    #был не ниже или левее, чем левый нижний угол другой фигуры.
    
    #Условия не_пересечения прямоугольников:    
    conditions = [rec1[0] >= rec2[2], rec1[1] >= rec2[3],
                  rec1[2] <= rec2[0], rec1[3] <= rec2[1]]
    
    return 'false' if any(conditions) else 'true'


# In[ ]:


rec1 = [0,0,1,1]
rec2 = [0,0,3,3]


# In[ ]:


get_ipython().run_line_magic('timeit', 'imposition(rec1, rec2)')


# In[ ]:


get_ipython().run_line_magic('timeit', 'imposition1(rec1, rec2)')

