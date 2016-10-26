import subprocess


def get_media_svn_revision(absolute_path):
    repo_dir = absolute_path
    svn_revision = subprocess.Popen(
        'svn info | grep "Revision" | awk \'{print $2}\'',
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        shell=True, cwd=repo_dir, universal_newlines=True
    )
    rev = svn_revision.communicate()[0].partition('\n')[0]
    return rev
