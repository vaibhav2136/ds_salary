# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 20:00:42 2023

@author: vibhu2134
"""

import glassdor_scraper as gs
import pandas as pd
  


path = r"C:\Users\91701\pythonProject\ds_salary_proj\chromedriver"


df = gs.get_jobs('data scientist', 15, False,path,15)
