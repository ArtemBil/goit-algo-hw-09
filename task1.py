def find_coins_greedy(amount, coins):
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count

    return result


def find_min_coins_dynamic(amount, coins):
    min_coins = [float('inf')] * (amount + 1)
    coin_used = [0] * (amount + 1)

    min_coins[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result


coins = [50, 25, 10, 5, 2, 1]
amount = 113

greedy_result = find_coins_greedy(amount, coins)
dp_result = find_min_coins_dynamic(amount, sorted(coins))

print(greedy_result)
print(dp_result)
