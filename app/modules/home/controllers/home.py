from flask import render_template
from app.modules.home.models.project import Project


class HomeController():
    def projects(self):
        url_prefix = "http://23.239.5.59:5000/"
        project1 = Project(name="dnd sleep spell calculator",
                           author="justinelinette",
                           date_posted="3/2/23",
                           img_src="/static/images/thumb_ss.png",
                           descr="calculate enemies affected by sleep spell in dnd 5e",
                           url=f"{url_prefix}sleep_spell")
        project2 = Project(name="film reviewer + scrobbler",
                           author="justinelinette",
                           date_posted="3/2/23",
                           img_src="/static/images/thumb_fs.png",
                           descr="scrobble, rate, review, and list streamed movies",
                           url=f"{url_prefix}film_scrobbler")
        projects = [project1, project2]
        return render_template("home.html", projects=projects)
