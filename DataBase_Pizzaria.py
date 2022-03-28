#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy  as np
import datetime as dt
import seaborn 
import matplotlib.pyplot as plt
import plotly.graph_objects as go


#Open a dataBase 
pizzaria_df = pd.read_csv(r"D:\Projetos bancos de dados\Pizzaria\Datafiniti_Pizza_Restaurants_and_the_Pizza_They_Sell_May19.csv")

#cleaning unnecessary data 
pizzaria_df = pizzaria_df.drop(['menuPageURL','postalCode','keys','dateAdded','dateUpdated','menus.dateSeen'],axis=1)
pizzaria_df = pizzaria_df[(pizzaria_df['menus.amountMax'] != 0) & (pizzaria_df['menus.amountMin'] != 0)]
display(pizzaria_df) 


# In[2]:


#Question 1:
'''
What are the categories of resturants? 
'''
categories = pizzaria_df['primaryCategories'].value_counts().reset_index().rename(columns ={'index' :'Primary Categories','primaryCategories':'Values'},                                                                                  index={0:1,1:2,2:3,3:4,4:5,5:6,6:7,7:8})
display(categories)
'''
Analysis:
you can see that there are several pizzerias that have different categories, such as
they serve pizzas and function as restaurants 
'''


# In[3]:


#Question 2:
'''
What are the 10 cities with the most pizzerias by province?  
'''
cities_for_provinces = pizzaria_df[['city','province']].value_counts().reset_index().rename(columns={0:'restaurants by city'},                                                                                     index={0:1,1:2,2:3,3:4,4:5,5:6,7:8,9:10})

cities_for_provinces_plot = pizzaria_df[['city']].value_counts().head(10).reset_index().rename(columns={0:'restaurants by city'},                                                                                               index={0:1,1:2,2:3,3:4,4:5,5:6,7:8,9:10}).plot('city','restaurants by city',kind='bar')

display(cities_for_provinces.head(10))
print('==='*40)                                                                                                                                                               


# In[4]:


#Question 3:
'''
top 10 frequented provinces 
'''
provinces = pizzaria_df['province'].value_counts().reset_index().rename(columns={'index':'provinces','province':'frequency '},                                                                    index={0:1,1:2,2:3,3:4,4:5,5:6,7:8,9:10})
plot_df= pizzaria_df['province'].value_counts().head(10).reset_index().rename(columns={'index':'provinces','province':'frequency'},                                                                      index={0:1,1:2,2:3,3:4,4:5,5:6,7:8,9:10}).plot('provinces','frequency',kind ='barh')

display(provinces.head(10))
                                                               
print('==='*40)


# In[5]:


#Question 4:
'''

'''
print('total franchises in the data set: {}'.format(len(np.unique(pizzaria_df['id']))))
restaurant_list = pizzaria_df['name'].value_counts().reset_index().rename(columns ={'index':'Name','name':'number of branches'},                                                                          index={0:1,1:2,2:3,3:4,4:5,5:6,7:8,9:10})

pizzaria_df['name'].value_counts().head(10).reset_index().rename(columns ={'index':'Name','name':'Values'}).plot('Name','Values',kind ='barh')
                                                       
display(restaurant_list.head(10))
print('==='*40) 


# In[6]:


#Question 5:
'''
Top 10 Pizza flavors 
'''
#Removed the 'pizza' line as it is generalized 
menu_pizza_df = pizzaria_df['menus.name'].value_counts().reset_index()
menu_pizza_df = menu_pizza_df.drop(menu_pizza_df.index[[4]])
menu_pizza_df = menu_pizza_df.rename(columns ={'index':'Name'},index={0:1,1:2,2:3,3:4})

display(menu_pizza_df.head(10))
print('==='*40) 

#I plotted by stages to remove the 'pizza' line 
menu_pizza_grapic_df = pizzaria_df['menus.name'].value_counts().head(10).reset_index().rename(columns ={'index':'Name'})                                                      
menu_pizza_grapic_df = menu_pizza_grapic_df.drop(menu_pizza_grapic_df.index[[4]])
menu_pizza_grapic_df.plot('Name','menus.name',kind='bar')  


# In[7]:


#Question 6:
'''
where can i find cheese pizza: 
'''
chesse_pizza_df =  pizzaria_df[pizzaria_df['menus.name'] == 'Cheese Pizza']
chesse_pizza_df.drop_duplicates('id',inplace = True)
chesse_pizza_df.shape
fig = go.Figure(data=go.Scattergeo(
        lon = chesse_pizza_df['longitude'],
        lat = chesse_pizza_df['latitude'],
        text = chesse_pizza_df['name'] + ' :-' + chesse_pizza_df['province'],
        mode = 'markers',
        
    
        marker_color = 'red',
        ))

fig.update_layout(
        title = 'Cheese Pizza',
        geo_scope='usa',
    )
fig.show()


# In[8]:


#Question 7:
'''
where is the most expansive and cheap pizza 
'''
expansive_pizza_df = pizzaria_df[['city','name','menus.name','menus.amountMin','longitude','latitude']][pizzaria_df['menus.amountMin'] == pizzaria_df['menus.amountMin'].max()]                                                                         .rename(columns={'menus.amountMin':'maximum value'},                                                                                index={3270:1,3285:2,3287:3,4774:4,4775:5})
display(expansive_pizza_df)

print('==='*40)

cheap_pizza_df = pizzaria_df[['city','name','menus.name','menus.amountMax','longitude','latitude']][pizzaria_df['menus.amountMax'] == pizzaria_df['menus.amountMax'].min()]                                                                         .rename(columns={'menus.amountMax':'minimum value'},                                                                                index={804:1,2777:2,2778:3,7827:4})

display(cheap_pizza_df)


print('==='*40)
all_values_df = expansive_pizza_df.merge(cheap_pizza_df,how='outer').rename(columns={'menus.amountMax':'minimum value','menus.amountMin':'maximum value'},                                                                         index={0:1,1:2,2:3,3:4,4:5,5:6,6:7,7:8,8:9})
display(all_values_df)

print('==='*40)

fig = go.Figure(data=go.Scattergeo(
        lon = all_values_df['longitude'],
        lat = all_values_df['latitude'],
        text = all_values_df['name'],
        mode = 'markers',
        
    
        marker_color = 'red',
        ))

fig.update_layout(
        title = 'Cheese Pizza',
        geo_scope='usa',
    )
fig.show()


# In[ ]:




