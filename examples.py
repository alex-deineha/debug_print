import numpy as np

if __name__ == '__main__':

    from debug_print import debug_print as dp

    loss = 3.333
    train = np.zeros((5, 13))
    dp(loss, train.shape)

    dp(np.sin(np.pi / 4), np.cos(np.pi / 4))

    some_list = [1, 2, 3, 'Hello!']
    dp(some_list, len(some_list))

    from debug_print import debug_print_with_type as dp

    loss = 3.333
    train = np.zeros((5, 13))
    dp(loss, train.shape)

    dp(np.sin(np.pi / 4), np.cos(np.pi / 4))

    some_list = [1, 2, 3, 'Hello!']
    dp(some_list, len(some_list))
