import pandas as pd

# load the csv
df=pd.read_csv("Resources\pybank_budget_data_fixed.csv")

# convert the Date column to a list
cnt = df.Date.tolist()

# create month and year columns from Date column
df["Month"] = [ x.split('-')[0] for x in cnt ]
df["Year"]= [ x.split('-')[1] for x in cnt ]

# Total months
tot_mnths= df.Month.describe()["count"]

# net total amount of "Profit/Losses" over the entire period
prft_tot = df["Profit/Losses"].sum()

#The average of the changes in "Profit/Losses" over the entire period
avg_prft= df["Profit/Losses"].mean()

#The greatest increase in profits (date and amount) over the entire period
prft_lis = df["Profit/Losses"].tolist()

collect = []
for val in range(len(prft_lis)-1):
    cur= prft_lis[val]
    sm = cur + prft_lis[val+1]
    collect.append(sm)

fnd_mx=max([(value,idx) for idx,value in enumerate(collect)])
mx_ind = cnt[fnd_mx[1]]


#The greatest decrease in losses (date and amount) over the entire period
fnd_min=min([(value,idx) for idx,value in enumerate(collect)])
mn_ind = cnt[fnd_min[1]]

if __name__ == "__main__":
    print("Financial Analysis")
    print("-------------------")
    print("Total Months: %s" % tot_mnths)
    print("Total:$%s" % prft_tot)
    print("Average Change: $ +%s" % avg_prft)
    print("Greatest increase in profits: %s (%s)" % (mx_ind,fnd_mx[0]))
    print("Greatest decrease in profits: %s (%s)" % (mn_ind,fnd_min[0]))
    