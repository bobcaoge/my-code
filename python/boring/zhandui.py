import time
from sendEmail import send_email
import pickle

class Team(object):
    def __init__(self):
        self.teams = {
            "zuisbuibu": 1,
            "kisdkjashk": 0,
            "bob": 2,
            "mjcgjSVHD": 3,
        }
        self.time = 1557721264

    def update(self, cur_time):
        self.time = cur_time
        for key in self.teams.keys():
            self.teams[key] = (self.teams[key]+1) % 4

    def get_info(self):
        team_name = ""
        for team, value in self.teams.items():
            if value == 2:
                team_name = team
                break
        return "The team that should be managed is {0}".format(team_name)

class Center(object):
    team = None
    def __init__(self):
        self.load_object()

    def load_object(self):
         with open("./data.data", "rb") as f:
            self.team = pickle.loads(f.read())

    def data_control_center(self):
        cur_time = time.time()
        if cur_time - self.team.time > 7*24*3600:
            self.team.update(cur_time)
            self.dump_object()
        print(self.team.get_info())

    def dump_object(self):
        try:
            with open("./data.data.tmp","wb") as fw:
                with open("./data.data", "rb") as fr:
                    fw.write(fr.read())
        except:
            send_email(content="文件存储失败")
        with open("./data.data", "wb") as f:
            f.write(pickle.dumps(self.team))


def main():
    # team = Team()
    # with open("./data.data", "wb") as f:
        # f.write(pickle.dumps(team))
    # with open("./data.data", "wb") as f:
        # t = pickle.loads(f.read())
        # print(t.time)
    center = Center()
    center.data_control_center()


if __name__ == '__main__':
    main()