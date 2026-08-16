import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd 
from streamlit_lottie import st_lottie

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
df=pd.read_csv("googleplaystore.csv")



# streamlit run "/media/sai-satyam/New Volume/Programming/Projects/ma'am projects/prac.py"

lottie_url = "https://lottie.host/4e8d1f22-b420-4473-a3a0-97f05dc2c02f/KGfTwHTy0u.json"


with st.sidebar:
    option_main = option_menu("CONTENTS",
                              ["MAIN", "DATASET", "DESCRIPTIVE ANALYSIS","VIZ HUB", "VIZ 1","VIZ 2"],
                              icons=["house", "database", "info-circle",  "bar-chart","book","eye","pencil","trash"],
                              menu_icon="list",
                              default_index=0)


if option_main == "MAIN":
    with st.expander("HEY OPEN IT!:)"):

        col1, col2 = st.columns([15,25])
        
        with col1:
            st.write("")
            st_lottie(lottie_url, key="user", width=365, height=-900)
            
        with col2:
            st.title(" GOOGLE PLAYSTORE APP ANALYSIS")
            st.markdown("""
    ### Welcome to the Google Play Store App Analysis! 
    Dive into the world of app ratings 📱, downloads, and sizes with our comprehensive analysis. Whether you're curious about the most popular apps or the trends in app pricing, we've got you covered! Let's explore and uncover insights together. 🚀✨
    """)

      


elif option_main == "DATASET":
    col1,col2=st.columns([15,25])
    with col1:
        link0="https://lottie.host/abaea818-8861-44c8-884c-8d7888810699/kScLGeM8LN.json"
        st_lottie(link0,key="user",width=365,height=150)
    with col2:
         st.title("All about datasets!!")
    a=st.selectbox("select dataset",options=["google playstore","user reviews"])
    if a=="google playstore":
        
        df=pd.read_csv("googleplaystore.csv")
        st.title(" Dataset")
        a=st.selectbox("VIEW",options=["View raw dataset","Brief info of the dataset","view number of missing values","view datatypes of the dataset","clean dataset"])
        if a=="View raw dataset":
            df = pd.read_csv("googleplaystore.csv")
            st.write(df)
        elif a=="Brief info of the dataset":
            st.title("Info of the dataset")
            st.write("Number of rows:", df.shape[0])
            st.write("Number of columns:", df.shape[1])
            st.write("Column names:", df.columns.tolist())
            st.write("Non null counts")
            st.table( df.count())
        elif a=="view number of missing values":
            st.title("Null values")
            st.table(df.isnull().sum())
            st.title("visual representation")
            plt.figure(figsize=(6, 4))
            st.write(sns.heatmap(df.isnull(),yticklabels=False,cbar=False))
            st.pyplot(plt)
        elif a=="view datatypes of the datasets":
            st.title("dtypes")
            st.table(df.dtypes)
        elif a=="clean dataset":
            st.write("choose what you want to displaly")
            b=st.selectbox("view",options=["cleaned dataset","datatypes"])

            if b=="cleaned dataset":
                df=pd.read_csv("Preprocessed_GPS.csv")
                st.write(df)
            elif b=="datatypes":
                df=pd.read_csv("Preprocessed_GPS.csv")
                st.table(df.dtypes)
    if a=="user reviews":
        df=pd.read_csv("googleplaystore_user_reviews.csv")
        st.title(" Dataset")
        a=st.selectbox("VIEW",options=["View raw dataset","Brief info of the dataset","view number of missing values","view datatypes of the dataset","clean dataset"])
        if a=="View raw dataset":
                df = pd.read_csv("googleplaystore_user_reviews.csv")
                st.write(df)
        elif a=="Brief info of the dataset":
                st.title("Info of the dataset")
                st.write("Number of rows:", df.shape[0])
                st.write("Number of columns:", df.shape[1])
                st.write("Column names:", df.columns.tolist())
                st.write("Non null counts")
                st.table( df.count())
        elif a=="view number of missing values":
                st.title("Null values")
                st.table(df.isnull().sum())
                st.title("visual representation")
                plt.figure(figsize=(6, 4))
                st.write(sns.heatmap(df.isnull(),yticklabels=False,cbar=False))
                st.pyplot(plt)
        elif a=="view datatypes of the dataset":
                st.title("dtypes")
                st.table(df.dtypes)
        elif a=="clean dataset":
                st.write("choose what you want to displaly")
                b=st.selectbox("view",options=["cleaned dataset","datatypes"])
                if b=="cleaned dataset":
                    df=pd.read_csv("Mergetdatasets.csv")
                    st.write(df)
                elif b=="datatypes":
                    df=pd.read_csv("Mergetdatasets.csv")
                    st.table(df.dtypes)
            

elif option_main == "DESCRIPTIVE ANALYSIS":
    link="https://lottie.host/273c7831-bcda-4296-9d2b-ab145375b316/PcxCfTTnEu.json"
    col1,col2,col3=st.columns([15,13,10])
    with col1:
        st_lottie(link,key="user",width=300,height=300)
    with col2:
        with st.form(key="dataset-info"):
          st.write("learn description about dataset")
          btn1=st.form_submit_button("LEARN MORE")
    if btn1:

            # Title for Play Store Analysis
        st.title("Google Play Store Analysis")

            # Play Store Dataset Information
        st.markdown("""
            **App**: The application's name and a brief description  
            **Category**: The app's assigned category  
            **Rating**: The average user rating  
            **Reviews**: The total number of user reviews  
            **Size**: The space the app occupies on a mobile phone  
            **Installs**: The overall installations or downloads  
            **Type**: Indicates whether the app is free or paid  
            **Price**: The installation cost. For free apps, the price is zero  
            **Content Rating**: Specifies if the app is suitable for all age groups  
            **Genres**: Various categories to which an app can belong  
            **Last Updated**: The date of the app's last update  
            **Current Ver**: The app's current version  
            **Android Ver**: The Android version supporting the app  
            """)

            # Add a horizontal rule for separation
        st.markdown("---")

            # Title for User Reviews Dataset
        st.title("User Reviews Dataset")

            # User Reviews Dataset Information
        st.markdown("""
            **App**: The app's name with a brief description  
            **Translated_Review**: English translation of the user's review  
            **Sentiment**: The reviewer’s attitude categorized as 'Positive', 'Negative', or 'Neutral'  
            **Sentiment_Polarity**: The review's polarity, ranging from -1 (Negative) to 1 (Positive)  
            **Sentiment_Subjectivity**: The score indicates the degree to which a reviewer’s opinion aligns with the general public’s opinion, with a range of [0, 1]. Higher scores suggest opinions closer to the general public, while lower scores indicate more factual information in the review  
            """)

          


             
        #   btn=st.form_submit_button("Read more")
    with col3:
          with st.form("description-info"):
            st.write("Here is the summary of my descriptive statastics of my dataset")
            btn3=st.form_submit_button("Read more")
    if btn3:

            st.title("Data Preprocessing Steps")

            with st.expander("Identifying Non-Numeric Reviews"):
                st.write("Checked and printed rows with nonnumeric characters in the 'Reviews' column.")

            with st.expander("Removing Irrelevant Row"):
                st.write("Dropped the row at index 10472 as it contained incorrect or irrelevant data, ensuring dataset integrity.")

            with st.expander("Converting Reviews to Integer"):
                st.write("Converted the 'Reviews' column to the integer data type for numerical analysis.")

            with st.expander("Converting Last Updated to Datetime"):
                st.write("Converted the 'Last Updated' column to datetime format for temporal analysis.")

            with st.expander("Handling Price Values"):
                st.write("Created a function (drop_dollar) to drop the '$' symbol and convert the 'Price' column to the float data type.")

            with st.expander("Handling Installs Values"):
                st.write("Created a function (drop_plus) to drop the '+' symbol and convert the 'Installs' column to the integer data type.")

            with st.expander("Converting Size Entries"):
                st.write("Created a function (kb_to_mb) to convert size entries to MB and handle 'k' or 'M' units.")

            with st.expander("Verifying Data Types"):
                st.write("Checked and printed the updated data type information after the type conversion.")

            with st.expander("Removing Duplicates"):
                st.write("Removed duplicate rows from both the Play Store and User Reviews datasets.")

            with st.expander("Handling Missing Values"):
                st.write("Filled missing values for numerical columns with the median and categorical columns with the mode. Checked and printed the updated number of missing values in both datasets.")

            with st.expander("Handling Outliers"):
                st.write("Visualized outliers through box plots for Reviews and Installs. Removed outliers from the data based on the quantile range (5% to 95%) for Reviews and Installs.")

            with st.expander("Removing Unnecessary Columns"):
                st.write("Dropped the 'Current Ver' column in the Play Store Dataset and the 'Translated_Review' column in the User Reviews Dataset.")
elif option_main=="VIZ HUB":
     
     link1="https://lottie.host/8d009708-cb3c-4d8f-8536-d1d7790de87e/wgZQje80me.json"
     with st.expander("HEY WELCOME!:)"):

        col1, col2 = st.columns([15,25])
        
        with col1:
            st.write("")
            st_lottie(link1, key="user", width= 300, height=300)
            
        with col2:
            st.title("A hub for your visualizations.")
            st.markdown(""" ### Welcome to viz hub! 
"Connect the dots in your data with VizHub’s powerful visuals."
    """)
                        

elif option_main == "VIZ 1":
    with st.sidebar:
        option=option_menu("Choose the type of visualization",["Data analysis","Comparitive analysis part 1","Comparitive analysis part 2"])
      
    
    if option=="Data analysis":
            
            st.markdown("🧁 Great choice! Let's dive into some simple data analysis with box plots, correlation graphs, and histograms!")
            df=pd.read_csv("preprocessed_GPS.csv")
            # st.write(df)
            
            st.subheader("Data Analysis")
            #################################################################################################################################
            st.write("📦show boxplots of all the feature columns")
            
            import plotly.graph_objects as go
            from plotly.subplots import make_subplots

                # Create a subplot grid
            fig = make_subplots(
                    rows=3, cols=2,
                    subplot_titles=('Rating', 'Installs', 'Size in mb', 'Price'),
                    vertical_spacing=0.2,  # Adjust spacing between rows
                    horizontal_spacing=0.1  # Adjust spacing between columns
                )

                # Add box plots to the subplots
            fig.add_trace(go.Box(y=df['Rating'], name='Rating'), row=1, col=1)
            fig.add_trace(go.Box(y=df['Installs'], name='Installs'), row=1, col=2)
            fig.add_trace(go.Box(y=df['Size in mb'], name='Size in mb'), row=2, col=1)
            fig.add_trace(go.Box(y=df['Price'], name='Price'), row=2, col=2)
            fig.add_trace(go.Box(y=df['Reviews'], name='Reviews'),row=3,col=1)


                # Update layout
            fig.update_layout(
                    title_text="Box Plots of Various Features",
                    height=600,  # Adjust the height as needed
                    showlegend=False
            )


            st.plotly_chart(fig)
                
            # st.markdown("<h3 style='font-size: 14px;'>Show pairplot of all the feature columns</h3>", unsafe_allow_html=True)

            
            # pairplot = sns.pairplot(df[['Rating', 'Installs', 'Size in mb', 'Price']])
            
            # # Use the current figure for Streamlit
            # st.pyplot(pairplot.figure)
                
            # st.write("##Corelation graph")
            
            # plt.figure(figsize=(10,10))
            # cdf=df[['Rating','Installs','Size in mb','Price',"Reviews"]]
            # corr=cdf.corr()
            # plt.figure(figsize=(8,8))
            # sns.heatmap(corr,annot=True,cmap="mako",center=0)
            # st.pyplot(plt)
            # st.write("#Distribution of Ratings")
            
            import plotly.express as px
            fig=px.histogram(df,x="Rating",color_discrete_sequence=['indianred'] )# color of histogram bars)
            st.plotly_chart(fig)

            #count and category and installs category
            st.write("No.of apps in each category")
            
                        
            category_counts = df['Category'].value_counts().reset_index()
            category_counts.columns = ['Category', 'Apps']
            fig = px.bar(category_counts, x='Category', y='Apps',color="Category" ,title='Number of Apps in Each Category')
            st.plotly_chart(fig)




            ###############################################################################################################################
    elif option=="Comparitive analysis part 1":
                df=pd.read_csv("preprocessed_GPS.csv")
                st.markdown("Let's compare some data and uncover interesting insights!")
                st.subheader("Comparitive analysis")
                st.write(" Installs and Reviews relation")
                fig_lm = px.scatter(df, x='Reviews', y='Installs', trendline='ols', 
                    title='Reviews vs Installs with Linear Regression Line')

                st.plotly_chart(fig_lm)

                # plt.figure(figsize=(5,5)) # make figure size
                # sns.lmplot(x='Reviews', y='Installs', data=df)
                # st.pyplot(plt)
                        
                st.write("Distribution of Paid and Free Apps")#no.of paid and free based upn installs
                app_type_counts = df["Type"].value_counts().reset_index()
                app_type_counts.columns = ['Type', 'Count']

                # Pie chart for the distribution
                fig_pie = px.pie(app_type_counts, values='Count', names='Type',
                                title='Distribution of Paid and Free Apps',
                                color_discrete_sequence=px.colors.qualitative.Pastel)

                st.plotly_chart(fig_pie)

                st.subheader("Number of installs for Paid and Free Apps")
                st.subheader("Scatter Plot")

                # Scatter plot for the number of installs
                fig_scatter = px.scatter(df, x='Type', y='Installs', color='Type',
                                        title='Number of Installs for Paid and Free Apps',
                                        height=600)

                st.plotly_chart(fig_scatter)

                st.subheader("Bar Plot")

                # Bar plot for the number of installs
                fig_bar = px.bar(df, x='Type', y='Installs', color='Type',
                                title='Number of Installs for Paid and Free Apps',
                                height=600)

                st.plotly_chart(fig_bar)
                                
                        


                st.write("Top 10 genres by installs")
                            
                df_genres_installs = pd.pivot_table(df, index="Genres", values=["Installs"], aggfunc='sum')
                df_genres_installs_sorted = df_genres_installs.sort_values(by="Installs", ascending=False)
                top_10_genres = df_genres_installs_sorted.head(10)

            # Create a heatmap using Plotly
                fig = px.imshow(top_10_genres, 
                            aspect="auto", 
                            color_continuous_scale='viridis', 
                            labels=dict(x="Genres", y="Installs"),
                            title='Top 10 Genres by Installs')

            # Display the heatmap in Streamlit
                st.plotly_chart(fig)


                st.write("top 10 Content Rating by Installs")
                
                fig = px.scatter(df, x="Content Rating", y="Installs", size="Reviews", color="Category",
                                            hover_name="App", size_max=60)
                            
                st.plotly_chart(fig)
                        
                st.write("Distributions of Ratings by Update Year")

                
                fig_reg = px.scatter(df, x='Update year', y='Rating', trendline='ols',
                     title='Rating vs Update Year with Linear Regression Line',
                     labels={'Update year': 'Update Year', 'Rating': 'Rating'})

                st.plotly_chart(fig_reg)

                # 3D scatter plot using Plotly
                st.write("Distribution of Reviews, Rating, and Installs with Update Year")

                fig_3d = px.scatter_3d(df, x='Update year', y='Reviews', z='Installs', color='Category',
                                    title='3D Scatter Plot of Reviews, Rating, and Installs with Update Year',
                                    labels={'Update year': 'Update Year', 'Reviews': 'Reviews', 'Installs': 'Installs'})

                st.plotly_chart(fig_3d)


                st.write("Top 10 Categories by Average Revenue")
                                    
              # Group by Category and calculate the mean Revenue, then sort and get the top 10
                category_revenue = df.groupby("Category")["Revenue"].mean().sort_values(ascending=False).head(10).reset_index()

                # Create a bar plot using Plotly
                fig_bar = px.bar(category_revenue, x='Category', y='Revenue', 
                                title='Top 10 Categories by Average Revenue', 
                                labels={'Category': 'Category', 'Revenue': 'Average Revenue'},
                                color='Category')

                # Display the bar plot in Streamlit
                st.plotly_chart(fig_bar)
            
            
    elif option=="Comparitive analysis part 2":
                df=pd.read_csv("preprocessed_GPS.csv")
                st.markdown("Let's compare some data and uncover interesting insights!")
                st.subheader("Comparitive analysis")
                         
                st.write("top 10 highest rated paid apps")
            

                filtered_df = df[df['Type'] == 'Paid'].sort_values(by='Reviews', ascending=False).head(5)

                    # Define stages and values for the funnel chart
                stages = filtered_df['App']
                values = filtered_df['Reviews']

                fig = px.scatter(filtered_df,
                                    x='Rating',
                                    y='App',
                                    size='Installs',  # Replace 'Downloads' with your actual column if available
                                    color='Reviews',
                                    title='Top 5 Highest Rated Paid Apps with Bubble Size Representing Reviews',
                                    labels={'App': 'App', 'Rating': 'Rating'},
                                    height=600)
                    # Show the chart
                st.plotly_chart(fig)

                    
                        
                st.write("top 10 highest rated Free Apps")
                colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#FF8F33', '#8FFF33', '#33FFF5', '#A633FF', '#FF3333', '#33FFBD']
                filtered_df = df[df['Type'] == 'Free'].sort_values(by='Rating', ascending=False).head(5)

                filtered_df = df[df['Type'] == 'Free'].sort_values(by='Rating', ascending=False).head(10)

                # Define stages and values for the funnel chart
                stages = filtered_df['App']
                values = filtered_df['Rating']

                # Create the pie chart
                pie_fig = go.Figure(go.Pie(
                    labels=stages,
                    values=values,
                    textinfo="label+value+percent",
                    hovertemplate='<b>%{label}</b><br>Rating: %{value}<br>Percent: %{percent:.2%}<extra></extra>',
                    marker=dict(colors=colors)
                ))

                # Update the layout
                pie_fig.update_layout(
                    title="Pie Chart of Top 10 Highest Rated Free Apps"
                )

                # Show the pie chart
                st.plotly_chart(pie_fig)

                st.write("top 5 free apps with highest number of reviews")
                filtered_df = df[df['Type'] == 'Free'].sort_values(by='Reviews', ascending=False).head(10)

                # Define stages and values for the funnel chart
                stages = filtered_df['App']
                values = filtered_df['Reviews']

                fig = px.scatter(filtered_df,
                                x='Rating',
                                y='App',
                                size='Installs',  # Replace 'Downloads' with your actual column if available
                                color='Reviews',
                                title='Top 5 Highest Rated Free Apps with Bubble Size Representing Reviews',
                                labels={'App': 'App', 'Rating': 'Rating'},
                                height=600)

                # Show the chart
                st.plotly_chart(fig)

                st.write("top 5 highest reviewed paid apps")
                                
                filtered_df = df[df['Type'] == 'Paid'].sort_values(by='Reviews', ascending=False).head(5)

                # Define stages and values for the funnel chart
                stages = filtered_df['App']
                values = filtered_df['Reviews']

                # Create the pie chart
                pie_fig = go.Figure(go.Pie(
                    labels=stages,
                    values=values,
                    textinfo="label+value+percent",
                    hovertemplate='<b>%{label}</b><br>Reviews: %{value}<br>Percent: %{percent:.2%}<extra></extra>',
                    marker=dict(colors=colors,line=dict(color='#000000', width=2))
                ))

                # Update the layout
                pie_fig.update_layout(
                    title="Pie Chart of Top 5 Highest Reveiwed paid Apps"
                )

                # Show the pie chart
                st.plotly_chart(pie_fig)

        
                st.write("Total Revenue vs Total Installs")
                category_agg = df.groupby('Category').agg({'Revenue': 'mean', 'Installs': 'sum'})

                category_agg = category_agg.sort_values(by='Revenue', ascending=False).head(10)

                print(category_agg)
                fig = px.scatter(category_agg, x="Revenue", y="Installs", color=category_agg.index,
                 size="Revenue", hover_data=[category_agg.index],
                 title='Total Revenue vs. Total Installs by Category')

                # Show the plot
                st.plotly_chart(fig)


                st.write("Sum of Installs vs Reviews")
                category_agg = df.groupby('Category').agg({'Revenue': 'mean', 'Installs': 'sum','Reviews':'mean','Rating':'mean'})

                category_agg = category_agg.sort_values(by='Revenue', ascending=False).head(10)

                print(category_agg)


                fig = px.scatter(category_agg, x="Revenue", y="Installs", size="Reviews", color=category_agg.index,
                                hover_name="Rating", size_max=60,labels={'color':'Category'})

                # Show the plot
                st.plotly_chart(fig)
                st.write("Sum of installs vs reviews")
                fig = px.histogram(df, x="Reviews", y="Installs")
                st.plotly_chart(fig)
                st.write("Distributions of App reviews vs Installs")
                fig = px.scatter(df, x='Installs', y='Reviews', title='Distribution of App Reviews vs Installs',
                                labels={'Installs': 'Number of Installs', 'Reviews': 'Number of Reviews'},
                                hover_data=['App', 'Category'])
                st.plotly_chart(fig)
                st.write("Ratings distribution")
                fig = px.histogram(df, x="Rating", color="Category").update_xaxes(categoryorder='total descending')
                st.plotly_chart(fig)
                fig = px.histogram(df, x="Rating", color="Installs_category").update_xaxes(categoryorder='total descending')
                st.plotly_chart(fig)
    
elif option_main=="VIZ 2":
                    df2=pd.read_csv("googleplaystore_user_reviews.csv")
                    df2.drop_duplicates(inplace=True)
                    df2['Sentiment_Polarity'].fillna(df2['Sentiment_Polarity'].median(), inplace=True)
                    df2['Sentiment_Subjectivity'].fillna(df2['Sentiment_Subjectivity'].median(), inplace=True)
                    df2['Sentiment'].fillna(df2['Sentiment'].mode()[0], inplace=True)
                    df2['Translated_Review'].fillna('No review', inplace=True)
                    df2 = df2.drop('Translated_Review', axis=1)
                
                    st.title("sentiment distribution")
                    sns.set(style='whitegrid')

                    # Plot distribution of Sentiment Polarity
                    # Clear the figure
        
                    plt.figure(figsize=(10, 5))
                    plt.title('Distribution of Sentiment Polarity',size=20)
                    sns.histplot(df2['Sentiment_Polarity'], bins=50, kde=True)
                    plt.xlabel('Sentiment Polarity',size=15)
                    plt.ylabel('Frequency',size=15)
                    st.pyplot(plt)
                    st.title("sentiment count on category")
                    df0=pd.read_csv("preprocessed_GPS.csv")
                    
                    sns.set(style='whitegrid')

                    # Set the figure size
                    plt.figure(figsize=(14, 6))

                    # Merging the Play Store data with the User Reviews data
                    merged_df = pd.merge(df0, df2, on='App', how='inner')

                    # Calculating the average sentiment polarity for each app
                    average_sentiment_polarity = merged_df.groupby('App')['Sentiment_Polarity'].mean()

                    # Merging the average sentiment polarity back to the original play store dataframe
                    play_store_sentiment_df = df0.join(average_sentiment_polarity, on='App')

                    # Count the number of sentiments for each category
                    grouped_df = merged_df.groupby(['Category', 'Sentiment']).size().unstack()

                    sns.barplot(data=grouped_df.reset_index(), x='Category', y='Positive', color='skyblue', label='Positive')
                    sns.barplot(data=grouped_df.reset_index(), x='Category', y='Negative', color='gray', bottom=grouped_df['Positive'], label='Negative')
                    sns.barplot(data=grouped_df.reset_index(), x='Category', y='Neutral', color='orange', bottom=grouped_df['Positive'] + grouped_df['Negative'], label='Neutral')

                    # Adding labels and title
                    plt.xlabel('Category',size=15)
                    plt.xticks(rotation=90)
                    plt.ylabel('Count of Sentiments',size=15)
                    plt.title('Sentiments vs Category',size=20)

                    # Adding legend
                    plt.legend(title='Sentiment')

                    # Displaying the plot
                    st.pyplot(plt)

                    st.title("Progression of update counts and the distribution of sentiment counts over time")
                                       
                    update_counts = merged_df.groupby("Update year")["App"].count()

                    # Group by 'Update Year' and 'Sentiment' and count occurrences
                    sentiment_counts = merged_df.groupby(['Update year', 'Sentiment']).size().unstack()

                    # Plotting
                    plt.figure(figsize=(8, 8))

                    # Plotting the number of updates received
                    plt.subplot(2, 1, 1)
                    plt.plot(update_counts.index, update_counts, label='Number of Updates', marker='o', color='gray')
                    plt.ylabel('Number of Updates', size=15)
                    plt.title('Number of Updates and Sentiments over Update Years', size=15)
                    plt.legend()

                    # Plotting sentiments
                    plt.subplot(2, 1, 2)
                    plt.plot(sentiment_counts.index, sentiment_counts['Positive'], label='Positive', marker='o')
                    plt.plot(sentiment_counts.index, sentiment_counts['Negative'], label='Negative', marker='o')
                    plt.plot(sentiment_counts.index, sentiment_counts['Neutral'], label='Neutral', marker='o')
                    plt.xlabel('Update Year', size=15)
                    plt.ylabel('Number of Sentiments', size=15)
                    plt.legend()

                    # Adjust layout for better readability
                    plt.tight_layout()

                    # Show the plot
                    st.pyplot(plt)
                    st.title("relationship between sentiment polarity and installs")
                    sns.set(style='whitegrid')


                    plt.figure(figsize=(10, 5))

                    # Scatter plot with size based on the number of installs
                    sns.scatterplot(x='Rating', y='Sentiment_Polarity', size='Installs', data=play_store_sentiment_df, sizes=(50, 300), edgecolor='white',legend=True)

                    # Customize the plot
                    plt.title('Sentiment Polarity by Rating and Installs', size=15)
                    plt.xlabel('Rating', size=15)
                    plt.ylabel('Average Sentiment Polarity', size=15)

                    # Show the plot
                    st.pyplot(plt)
                    st.title("relationship between sentiment subjectivity and polarity")
                    # Chart - 13 visualization code
                    # Relationship between Sentiment Subjectivity and Sentiment Polarity
                    # Set the size of the figure
                    plt.figure(figsize=(12, 6))

                    # Create a scatter plot using seaborn
                    sns.scatterplot(data=merged_df, x='Sentiment_Subjectivity', y='Sentiment_Polarity', hue='Sentiment', palette='Set2')

                    # Set labels for the x and y axes
                    plt.xlabel('Sentiment Subjectivity', size=15)
                    plt.ylabel('Sentiment Polarity', size=15)

                    # Set the title of the plot
                    plt.title('Relationship between Sentiment Subjectivity and Sentiment Polarity', size=15)

                    # Display the plot
                    st.pyplot(plt)
                    st.title("final corelation heatmap")
                    numerical_columns = merged_df[['Rating', 'Reviews', 'Installs', 'Price', 'Sentiment_Polarity', 'Sentiment_Subjectivity']]

                    # Create a correlation matrix
                    correlation_matrix = numerical_columns.corr()

                    # Create a heatmap
                    plt.figure(figsize=(10, 5))
                    sns.heatmap(correlation_matrix, annot=True, cmap='rocket', fmt=".2f")
                    plt.title('Correlation Heatmap',size=20)
                    st.pyplot(plt)


     
     
                    





                    




# elif option_main == "REGISTER":
#     with st.form("register"): 
#         app = st.text_input("App")
#         category = st.text_input("Category")
#         rating = st.number_input("Rating")
#         reviews = st.text_input("Reviews")
#         size = st.number_input("Size")
#         installs = st.text_input("Installs")
#         type_ = st.text_input("Type")
#         price = st.text_input("Price")
#         content_rating = st.text_input("Content Rating")
#         genres = st.text_input("Genres")
#         last_updated = st.text_input("Last Updated")
#         current_ver = st.text_input("Current Ver")
#         android_ver = st.text_input("Android Ver")
#         b = st.form_submit_button("Submit")
        
#         if b:
#             st.write("Account created successfully")

# elif option_main== "READ":
#     data = database.getdata()
#     df = pd.DataFrame(data, columns=['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type,Price', 'Content Rating', 'Genres', 'Last Updated', 'Current Ver', 'Android Ver'])
#     st.dataframe(df)
