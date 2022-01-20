from field import dist


def transition(x_player, y_player, field_):
    for i in field_:
        if field_[i] == "2":
            if dist(x_player, y_player, i[0], i[1]) < 80:
                return True
            return False


def transition_4(x_player, y_player, field_):
    for i in field_:
        if dist(x_player, y_player, i[0], i[1]) < 100:
            return field_[i]
