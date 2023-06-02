import pandas as pd

def count_Degrees(df):
    # return a count of coders with Bachelor's & Masters degrees respectively.
    edu_list = df['EdLevel']
    bachelor_cnt = 0
    master_cnt = 0
    for item in edu_list:
        if type(item) == str:
            if "Bachelor" in item:
                bachelor_cnt += 1
            elif "Master" in item:
                master_cnt += 1
    return bachelor_cnt, master_cnt

def count_languages(df):
    # return dictionary of each languages coders know and the count of how many coder know that language.
    languages_list = df['LanguageHaveWorkedWith']
    language_count_dict = {}
    for response in languages_list:
        if type(response) == str:
            # User responses look like ex: C#;C++;HTML/CSS;JavaScript;Python
            # So seperate them into a new list to iterate through.
            all_languages = response.split(";")
            for language in all_languages:
                if language not in language_count_dict:
                    language_count_dict[language] = 0
                language_count_dict[language] += 1
    return language_count_dict

def main():
    # Prints results of counting degrees, programming languages, and count of ages per sexuality.
    df = pd.read_csv('stackoverflowdata/survey_results_public.csv')
    bachelor_count, master_count = count_Degrees(df)
    print(f"There are {bachelor_count} coders with Bachelor's degrees and \n{master_count} coders with Master's degrees.")
    print()

    language_count_dict = count_languages(df)
    for lang in language_count_dict:
        print(f"{language_count_dict[lang]} coders know {lang}.")
    print()

# print out amount of people per age & sexuality.
    age_sexuality_counts = df.groupby(['Age', 'Sexuality']).size().reset_index(name='Count')
    print(age_sexuality_counts)

main()