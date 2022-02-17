
num_cases = int(input())

for i in range(num_cases):
    num_songs = int(input())
    predicted_ratings = list(map(int, input().split()))
    like_dislike_string = input()

    initial_positions_dict = {}

    dislike_list = []
    like_list = []

    for j in range(num_songs):
        if like_dislike_string[j] == "0":
            dislike_list.append(predicted_ratings[j])
        else:
            like_list.append(predicted_ratings[j])
        
        initial_positions_dict[predicted_ratings[j]] = j
    
    dislike_list.sort()
    like_list.sort()

    predicted_ratings_sorted = dislike_list + like_list

    final_predict_list = [0] * num_songs
    
    new_predict = 1
    for value in predicted_ratings_sorted:
        final_predict_list[initial_positions_dict[value]] = new_predict
        new_predict += 1
    
    print(" ".join(list(map(str, final_predict_list))))




