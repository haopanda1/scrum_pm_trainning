# Databricks notebook source
# MAGIC %md 
# MAGIC
# MAGIC ### SCRUM Review

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC #### SCRUM Basics 
# MAGIC - one iteration is `two weeks`
# MAGIC - during two weeks period, your team need deliver the user stories with highest value
# MAGIC - to make sure your team is on trake, you need `daily standup` daily, 15 mins each
# MAGIC   - Objective 1: Organize tasks
# MAGIC   - Objective 2: asking for help
# MAGIC - the work of your team comes from `product owner`, the business representative of the team. 
# MAGIC   - **PO is the one who create user story, and your team is the one who create tasks for each user story**
# MAGIC - at the end of a sprint, your team will do a `sprint demo` the functional `MVP` developed
# MAGIC - after the `sprint demo`, your team will spend time and do a `retrospective`, a conversation regarding how to do better as a team. 
# MAGIC
# MAGIC #### PO & SCRUM Master 
# MAGIC - PO is focus on all feature / task the team can create; on the other side, SCRUM master is focus on protecting team and its performance
# MAGIC - these two roles should be in a healthy opposition

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC #### PO's Responsibility
# MAGIC - PO not only ensure the correct feature being delivered, but also make sure the team's need is met too
# MAGIC - team's success depends heavily on PO
# MAGIC - PO's duty
# MAGIC   - meet with stakeholders
# MAGIC   - ensure user story accurately describe business need
# MAGIC   - add clarification as the user story being developed
# MAGIC   - accept user stories from stakeholders
# MAGIC   - prioritize user stories 
# MAGIC   - help stakeholder understand why non-functional user story make sense
# MAGIC     - ie; stakeholders request ability for user login, the team need a non functional user story to create database. 
# MAGIC
# MAGIC #### Set Vision from Idea
# MAGIC - who to include when setting vizion 
# MAGIC   - stakeholders
# MAGIC   - sales 
# MAGIC   - tech people
# MAGIC
# MAGIC - What to discuss in vision session 
# MAGIC   - product name
# MAGIC   - product logo 
# MAGIC   - three to five key selling points
# MAGIC   - what is done for the product 
# MAGIC
# MAGIC #### Turn vision to roadmap 
# MAGIC - Roadmapping session 
# MAGIC   - you will need product owner, scrum master, and team members; Subject matter expert and stakeholders are optional
# MAGIC   - determine features

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC ### Product Owner

# COMMAND ----------

# MAGIC %md 
# MAGIC #### `product owner` is 
# MAGIC - responsible for the direction of team 
# MAGIC - own the relationship with stakeholders
# MAGIC - set the vision for the final product so everyone know what needs to be built
# MAGIC - create the roadmap so everyone know how to attain the vision
# MAGIC - determine works to create `MVP`
# MAGIC     - `MVP` allows the team to get the feedback from stakholder faster
# MAGIC     - `MVP` feedback will further create new user story

# COMMAND ----------

# MAGIC %md 
# MAGIC #### Roadmap Session
# MAGIC - ![roadmap](https://www.slideteam.net/media/catalog/product/cache/1280x720/6/_/6_months_scrum_roadmap_for_product_development_slide01.jpg)
# MAGIC   - each theme doesn't have to be finished in one Quarter / month, you can come back at any quarter/month
# MAGIC   - **Roadmap is not a commitment but an estimation. it can be updated along the project cycle**
# MAGIC

# COMMAND ----------

# MAGIC %md 
# MAGIC #### Dealing with Failed Sprint
# MAGIC - There are cases when stakeholder think a certain sprint is fail to deliver what they want
# MAGIC - how to deal with it? 
# MAGIC   - ask whether they think user story is good
# MAGIC   - ask if they agree with the acceptance critiria of the user story

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC #### Create Good User Story
# MAGIC - Epic story is the first level
# MAGIC   - it is a mucher larger story need to be broken down to user story
# MAGIC - Function based analysis
# MAGIC   - use `CRUD - Create, Read, Update, and Delete` to break down EPIC user story
# MAGIC   - example
# MAGIC     - EPIC Level US: as a sales person i want to manage my client so that value
# MAGIC     - Create; as a sales person I want to create a database so that I can append new client into my client list
# MAGIC - Steps in Process 
# MAGIC   - example 
# MAGIC     - login, browze avaliable courses, payment
# MAGIC
# MAGIC #### Release Plan 
# MAGIC - A detailed timeline of when functions / themes will be released
# MAGIC - Attendee of Release Plan Meeting 
# MAGIC   - team 
# MAGIC   - PO 
# MAGIC   - SM 
# MAGIC   - subject matter expert
# MAGIC   - key stakeholders
# MAGIC - Function Based Release Plan 
# MAGIC   - Stakeholders ask to deliver certain set of themes / features
# MAGIC   - your release plan is based on those themes / features
# MAGIC
# MAGIC #### Keep Backlog Up to date
# MAGIC - Meeting 1: Sprint Pre-Planning 
# MAGIC   - All team show up 
# MAGIC   - PO breif the team of upcoming user stories & team raise question of acceptance critiria of user story
# MAGIC - Meeting 2: Backlog Refinement
# MAGIC   - Subset of the team 
# MAGIC   - PO and SCRUM Master update, remove, and create new user stories

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC ### SCRUM Master

# COMMAND ----------

# MAGIC %md
# MAGIC #### SCRUM Master is 
# MAGIC - Solely focus on the team
# MAGIC - the process owner of the team
# MAGIC - the protector of the SCRUM framework & the team (limiting the distraction and keep team from overcommitting)
# MAGIC - the facilitator of daily meeting

# COMMAND ----------

# MAGIC %md
# MAGIC #### Stages of Team Development
# MAGIC - Forming; Team members get to know each other
# MAGIC   - SM need anticipate team member's questions
# MAGIC   - SM need repeat the purpose and Vision
# MAGIC   - SM need hold 1 on 1 conversation with each team members
# MAGIC   - **the goal of this stage is enable team member feel safe to challenge each other**
# MAGIC - Storming 
# MAGIC   - team member is able to challege team mate and questioning PO / SM 
# MAGIC - Norming
# MAGIC   - challeges in previous stage can bring harmony in norming stage
# MAGIC   - team member take personal responsibility
# MAGIC   - enjoy challenge conversation
# MAGIC - Performing
# MAGIC   - help you team member to be servant leader for other teams
