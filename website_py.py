import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


df=pd.read_csv(f"C:/Users/91626/Documents/GitHub/LinkedInJobAnalytics.github.io/final_Linked_Project_final_Output_DataFrame_final (1).csv")

df_skills_req=pd.read_csv(f"C:/Users/91626/Documents/GitHub/LinkedInJobAnalytics.github.io/skills (1) (1).csv")

pre_skills = df_skills_req['skills'].values

skill_df=pd.DataFrame(pre_skills,columns=['skills'])


# --------------------------------------------------------
skill_array_for_fuzzy_wuzzy=skill_df['skills']
lst=[]
for i in skill_array_for_fuzzy_wuzzy:
    lst.append(i)
# ---------------------------------------------------------------


def Input_return(lis):
    s=''
    for i in lis:
        s=s+' '+i
    return s 



def input_match(x):
    final_keyword = []
    input_variable = []
    input_variable.append(x)
    choices = lst
    for i in input_variable: 
        a = process.extract(i, choices)
        first_match = a[0] 
        convert_list = list(first_match)
        final_keyword.append(convert_list[0])
        final_keyword=final_keyword[0]
    # print(final_keyword)
    return(final_keyword)



def Checking_In_Our_Skills(s):
    if (df[df.skills.str.contains(s)].count()[0]>1):
        return True
    else:
        return False
# from fuzzywuzzy import process5
# query = 'pytonssm'
# choices = lst
# # Get a list of matches ordered by score, default limit to 5
# a = process.extract(query, choices)




def multi_output(skills):
    sum_of_job=[]
    class_list=[]
    industry_list=[]
    level_list=[]
    for i in skills:
        no_of_job = df[(df['Job_skills'].str.contains(i))| (df['skills_skills'].str.contains(i)) | (df["skills"].str.contains(i))]
        sum_of_job.append(len(no_of_job))
        Class = df[(df['Job_skills'].str.contains(i) )  | ( df['skills_skills'].str.contains(i)) | (df["skills"].str.contains(i))]['Class'].value_counts()
        Class=Class.reset_index()
        c=Class.iloc[0].values
        class_list.append(c)
        industry = df[(df['Job_skills'].str.contains(i) )  | ( df['skills_skills'].str.contains(i)) | (df["skills"].str.contains(i))]['Industry'].value_counts()
        industry =industry.reset_index()
        ind=industry.iloc[0].values
        industry_list.append(ind)
        level = df[(df['Job_skills'].str.contains(i) )  | ( df['skills_skills'].str.contains(i)) | (df["skills"].str.contains(i))]['Level'].value_counts()
        level =level.reset_index()
        lev = level.iloc[0].values
        level_list.append(lev)
    Class_df=pd.DataFrame(class_list,columns=['class','value_counts'])
    Class=Class_df.max()["class"]
    industry_df=pd.DataFrame(industry_list,columns=['industry','value_counts'])
    industry=industry_df.max()['industry']
    level_df=pd.DataFrame(level_list,columns=['level','value_counts'])
    level=level_df.max()['level']
    return ['count-->',sum(sum_of_job)],['Class-->',Class],['Industry-->',industry],['Level-->',level]


def Output_df(skills):
    for no,each in enumerate(skills):
        df_=df[(df['Job_skills'].str.contains(each)) | (df['skills_skills'].str.contains(each)) | (df["skills"].str.contains(each))]
        df_.drop(['Employees','Followers','Involvment',"Job_Desception",'skills','Job_skills','skills_skills'],axis=1,inplace=True,errors='ignore')
        df_=df_.reset_index()
        df_.drop('index',axis=1,inplace=True,errors='ignore')
        if (no == 0):
            final_df=df_
        else:
            final_df = pd.concat([final_df, df_], axis=0)
    final_df=final_df.reset_index()
    final_df.drop('index',axis=1,inplace=True,errors='ignore')
    return final_df









from flask import Flask,render_template, request, redirect, url_for, session
app = Flask(__name__)

app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def input():
    lower_input=[]
    s=None
    count=None
    class1=None
    industry=None
    level=None
    if request.method == 'POST':
        inp = request.form['input']
        inp = list(inp.split(','))
        inp=set(inp)
        print(inp)
        inp=list(inp)
        print(inp)
        for i in inp:
            i=i.strip()
            i=input_match(i)
            lower_input.append(i)
            print("lower_input----",lower_input)
            if i in pre_skills:
                print('passing')
                pass
            elif Checking_In_Our_Skills(i):
                print('skill is present in skills_column')
            else:
                lower_input.remove(i)
                print('remove this input',i)
        try:
            output = multi_output(lower_input)
        except:
            print('Something Is Not working in multi_output function () ')
            output=None
        s=Input_return(lower_input)
        print('printing the value of s --->',s)
        result=output
        print(result)
        count =result[0][1]
        class1 =result[1][1]
        industry=  result[2][1]
        level=result[3][1]
        session['my_list']=lower_input
    return render_template('input.html',sharing_input=s,lower_input=lower_input,count=count,class1=class1,industry=industry,level=level)

@app.route('/table')
def home():
    skills=session.get('my_list')
    # create a sample DataFrame
    df_=Output_df(skills)
    print(df_)
    # convert the DataFrame to an HTML table
    table_html = df_.to_html()
    print(table_html)

    # pass the HTML table to the template using render_template function
    return render_template('table_html.html', table_html=table_html)

# @app.route('/all_jobs')
# def all_jobs():
#     # convert the DataFrame to an HTML table
#     table_html = df.to_html()
#     print(table_html)

#     # pass the HTML table to the template using render_template function
#     return render_template('all_jobs.html', table_html=table_html)










if __name__ == '__main__':
    app.run(debug=True)
