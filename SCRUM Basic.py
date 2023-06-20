# Databricks notebook source
# MAGIC %md 
# MAGIC
# MAGIC ### Problem to Solve

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC [<img src="https://kanbanzone.com/wp-content/uploads/2020/08/agile-manifesto.png">](https://kanbanzone.com/wp-content/uploads/2020/08/agile-manifesto.png)
# MAGIC
# MAGIC ##### Scrum 
# MAGIC - Issues with Traditional Approach
# MAGIC   - Project work is unpredictable
# MAGIC - What SCRUM can do
# MAGIC   - Agile project management allows a team to adapt to change in real time
# MAGIC   - **The core objective is to winning each milestone of the project**
# MAGIC
# MAGIC ##### Waterfall Approach vs Agile
# MAGIC - for project like building a house, you can definitly plan ahead and build according to plan. hence `waterfall`
# MAGIC - for project like software development, you need a lot of trail and error, hence `agaile` 
# MAGIC
# MAGIC ##### Agile Manifesto & Theology
# MAGIC - In `Agile`, we ask business partners work with us along the way (no just beginning). 
# MAGIC - **The core idea is fail fast**
# MAGIC   - So that we have `small scale focus & rapid learning cycles`
# MAGIC
# MAGIC ##### SCRUM Framework
# MAGIC - Product owner select a backlog of work for the team
# MAGIC - A project cycle is `2 weeks`, team need review the backlog and see what they can do in the following two weeks
# MAGIC - within a project, Team develops and tests solutions until done
# MAGIC - At the end of two weeks, team need demonstrate what it accomplished to stakeholder & reflect what can be improved

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC ##### Waterfall Approach - Disadvantages - You are unable to change the following
# MAGIC - `Time`: Fixed & not able to change
# MAGIC - `Cost`: Fixed & not able to change
# MAGIC - `Scope`: Fixed & not able to change
# MAGIC
# MAGIC ##### Agile Approach - What it trying to change - LOCK EVERYTHING BUT SCOPE
# MAGIC - `Time`: Fixed & not able to change
# MAGIC - `Cost`: Fixed & not able to change
# MAGIC - `Scope`: **changable** bussiness can use the team in given time & cost to build what they think is valuable 
# MAGIC
# MAGIC ##### Two Key Roles in Agile
# MAGIC - **Product Owner**
# MAGIC   - Business rep dedicate 100% of his time to the team
# MAGIC   - Review Team's work to determine whether a team member's work is accepted or rejected
# MAGIC   - Ensure the team member understand the detail of the project
# MAGIC   - Interact with stakeholders on daily basis
# MAGIC   - **Keeper of product vision - what need to be done**
# MAGIC
# MAGIC   
# MAGIC - **SCRUM Master**
# MAGIC   - dedicate & protect team to work undistracted (guardrail of team)
# MAGIC   - ensure team doesn't burn out before the end of sprint
# MAGIC   - act like spokesperson for the team
# MAGIC   - **How to team does the work**
# MAGIC
# MAGIC ##### Time Duration in Agile
# MAGIC   - Two Weeks
# MAGIC   - **Daily Standup is needed for updating**
# MAGIC   - **Sprint Celebration Needed** 
# MAGIC
# MAGIC ##### Idea Team Compostion
# MAGIC   - Seven Member +/- two members
# MAGIC   - Maximize the communication between team
# MAGIC   - You need a team member with T -shape skills (has broad knowledge in multiple areas and deep knowledge in specific area)
# MAGIC
# MAGIC ##### Team Norms
# MAGIC   - working relationship 
# MAGIC   - conflict resolution
# MAGIC   - desire consensus

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC ##### Product Vision
# MAGIC - MVP (Minimum Viable Product)
# MAGIC   - An application that meets the bare minimium functionality & send to customer for feedback
# MAGIC   - ie: a food delivery app
# MAGIC   - *Why we need MVP*
# MAGIC     - The faster we get product to customer's hand, the faster we get feedback
# MAGIC     - We can aviod unnessisary function added to our application along the way
# MAGIC - Project Theme
# MAGIC   - When developing MVP of an application, we need seperate MVP into themes
# MAGIC   - AKA component of MVP
# MAGIC   - ie: payment, users, UI
# MAGIC   - *Why we need Theme*
# MAGIC     - Theme seperate works into categories that allows team to brainstorm
# MAGIC     - Theme can group works efficiently
# MAGIC - Theme's Feature
# MAGIC   - In each theme of MVP, we need breakdown to features
# MAGIC   - ie of payment theme: login, save password, recent orders, favorite, etc
# MAGIC   - by using features, product owners can identify what are features need to be developed in a sprint
# MAGIC
# MAGIC ##### User Stories
# MAGIC - detailed, valuable chunk of work a team can quickly deliver
# MAGIC - Anyone in the team can write user story, but it is usually PO
# MAGIC - **`INVEST` Rule of writting user story**
# MAGIC   - `Independent`: user story can be delivered independently from other user story
# MAGIC   - `Negotiable`: User story can be rewrite / canceled at anytime
# MAGIC   - `Valuable`: user story need to deliver value to stakeholders
# MAGIC   - `Estimable`: user story need to be estimable in form of `story point`
# MAGIC   - `Small`: user story need to be able to complete in 2 weeks
# MAGIC   - `Testable`: you are able to test the user story
# MAGIC - **User Story Format**
# MAGIC   - `AS A <role of user>, I want <what this user story is trying to achieve>, so that <what value can be created>`
# MAGIC   - *Functional User Story*
# MAGIC     - user story serves a function to end user
# MAGIC     - ie: As a mobile customer, I want the ability to create user profile so that order can be placed faster
# MAGIC   - *Non Functional User Story*: 
# MAGIC     - user story that support users without directly benifit them
# MAGIC     - ie: As a developer, I want to upgrade the database so that we have a supported product
# MAGIC - **Acceptance Critiria**
# MAGIC   - each user story must have acceptance critiria
# MAGIC   - ie: customer's email is able to be captured and saved
# MAGIC
# MAGIC ##### Team Boundary
# MAGIC - on ALL project level, has to be broad
# MAGIC - Components of Boundaries
# MAGIC   - definition of done
# MAGIC     - for user stories to consider done, it has be to tested in preprod environment
# MAGIC   - backlog prioritization 
# MAGIC     - Product owner need prioritize backlog
# MAGIC     - user stories rank based on value, we want to deliver the most value items first
# MAGIC   - sprint cadence
# MAGIC     - establish your sprint duration
# MAGIC
# MAGIC ##### Story Point Estimation
# MAGIC - Actual Estimation
# MAGIC   - specific, such as 20 hours for a user story
# MAGIC - Relative Estimation
# MAGIC   - estimation get via compare user stories against each other
# MAGIC
# MAGIC ##### Roadmap and Release Plan 
# MAGIC - Roadmap
# MAGIC   - it is on high level and map out when each theme will be worked on. considering dependency and sequence
# MAGIC - Release Plan
# MAGIC   - Release plan is related to maximize the story point in each sprint
# MAGIC   
# MAGIC

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC ##### Sprint Planning Meeting
# MAGIC - objective: 
# MAGIC   - each member understand the story and acceptance critiria of each story
# MAGIC   - set `team's definition of done` for each sprint
# MAGIC
# MAGIC ##### Sprint Review Session 
# MAGIC - Unaccepted / incomplete user stories are moved to next sprint, reviewed, and prioritized
# MAGIC - understand what is done and can be demonstrated to stakeholders
# MAGIC
# MAGIC ##### Demo Session 
# MAGIC
# MAGIC ##### Retrospective
# MAGIC - meeting focued on team performance at the end of each sprint
# MAGIC
