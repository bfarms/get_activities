import pandas as pd

def main():
	df = pd.read_csv('https://us.agworld.co/user_reports/2598/export.csv?api_token=Z3p6D3a2rU7HeVp3XOZhKg', sep=',', error_bad_lines=False, header=0, index_col=False, dtype='unicode')
	df.to_csv('all_activities.csv')
	print("Done.")

if __name__ == "__main__":
	main()