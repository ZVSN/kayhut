import utils

if __name__ == "__main__":
    j_file = "team.json"
    currTeamObj = utils.JsonFile

    team = currTeamObj.getData(j_file)
    if team != False:
        print("\nPrint all person's names that live at Berlin:")
        for currIndividual in team:
            if currIndividual['type'] == "Person" and currIndividual['city'] == "Berlin":
                print(currIndividual['name'])

        print("\nPrint all workers names which speak English:")
        for currIndividual in team:
            if currIndividual['type'] == "Worker":
                if 'English' in ' '.join(currIndividual['language'][0:]):
                    print(currIndividual['name'])

        print("\nPrint all workers and students names which age is lower than 40:")
        for currIndividual in team:
            if currIndividual['type'] == "Worker" or currIndividual['type'] == "Student" and currIndividual['age'] < 40:
                print(currIndividual['name'])


        print("\nPrint all individual surnames that their first names start with 'M' and their last name ends with 'g':")
        for currIndividual in team:
            if currIndividual['name'].startswith("M") == True and currIndividual['name'].endswith("g") == True:
                print(currIndividual['name'].split(' ')[1])

        print("\n")