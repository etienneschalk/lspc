# All information on the "sample" folder

root = "./sample/"

file_information = [
{
    "lines": 17,
    "words": 16,
    "bytes": 39,
    "path": "file0",
    "name": "file0",
    "hidden" : False
}, {
    "lines": 0,
    "words": 0,
    "bytes": 0,
    "path": "dir1/.dir1_filehidden",
    "name": ".dir1_filehidden",
    "hidden": True
}, {
    "lines": 1,
    "words": 1,
    "bytes": 2,
    "path": "dir1/dir1_file0",
    "name": "dir1_file0",
    "hidden" : False
}, {
    "lines": 1,
    "words": 1,
    "bytes": 9,
    "path": "dir2/dir2_A/dir2_A_file0",
    "name": "dir2_A_file0",
    "hidden" : False
}, {
    "lines": 2,
    "words": 2,
    "bytes": 18,
    "path": "dir2/dir2_A/dir2_A_file1",
    "name": "dir2_A_file1",
    "hidden" : False
}, {
    "lines": 0,
    "words": 0,
    "bytes": 0,
    "path": ".dirhidden/.dirhidden_filehidden",
    "name": ".dirhidden_filehidden",
    "hidden" : True
}, {
    "lines": None,
    "words": None,
    "bytes": 10241024,
    "path": "dir2/dir2_B/dir2_B_filebig",
    "name": "dir2_B_filebig",
    "hidden" : False
}
]

directory_information = [
{
    "path": "",
    "name": "",
    "nb_files": 1,
    "nb_dir": 3,
    "nb_files_all": 1,
    "nb_dir_all": 4,
    "hidden" : False
}, {
    "path": "dir0",
    "name": "dir0",
    "nb_files": 0,
    "nb_dir": 0,
    "nb_files_all": 0,
    "nb_dir_all": 0,
    "hidden" : False
}, {
    "path": "dir1",
    "name": "dir1",
    "nb_files": 1,
    "nb_dir": 1,
    "nb_files_all": 2,
    "nb_dir_all": 1,
    "hidden" : False
}, {
    "path": "dir2",
    "name": "dir2",
    "nb_files": 0,
    "nb_dir": 2,
    "nb_files_all": 0,
    "nb_dir_all": 0,
    "hidden" : False
}, {
    "path": "dir1/dir1_A",
    "name": "dir1_A",
    "nb_files": 0,
    "nb_dir": 0,
    "nb_files_all": 0,
    "nb_dir_all": 0,
    "hidden" : False
}, {
    "path": "dir2/dir2_A",
    "name": "dir2_A",
    "nb_files": 2,
    "nb_dir": 0,
    "nb_files_all": 2,
    "nb_dir_all": 0,
    "hidden" : False
}, {
    "path": "dir2/dir2_B",
    "name": "dir2_B",
    "nb_files": 1,
    "nb_dir": 0,
    "nb_files_all": 1,
    "nb_dir_all": 0,
    "hidden" : False
}, {
    "path": ".dirhidden",
    "name": ".dirhidden",
    "nb_files": 0,
    "nb_dir": 0,
    "nb_files_all": 1,
    "nb_dir_all": 0,
    "hidden" : True
}
]

# 6 options = 64 combinations
options = "Racldr"
# -d option overrides l and c
# -> we can eliminate 3 * 8 = 24 non-sense combinations
# ( d[Rar]lc -> l = false, c = false for each of the 8 [Rar] combinations)
# 64 - 24 = 40 combinations

# Moreover, the l and c options only display information already known in
# file_information and directory_information -> the list displayed are the same
# but with extra info to test -> 16 combinations to test, with 4 info variants

# The folders are always displayed before files.
predicted_lists_simple = {
    "": [
        "dir0", "dir1", "dir2", "file0"
    ],
    "a": [
        ".dirhidden", "dir0", "dir1", "dir2", "file0"
    ],
    "r": [
        "dir2", "dir1", "dir0", "file0"
    ],
    "ar": [
        "dir2", "dir1", "dir0", ".dirhidden", "file0"
    ]
}

predicted_lists_simple_directories = {
    "d": [
        "dir0", "dir1", "dir2"
    ],
    "rd": [
        "dir2", "dir1", "dir0"
    ],
    "ad": [
        ".dirhidden", "dir0", "dir1", "dir2"
    ],
    "ard": [
        "dir2", "dir1", "dir0", ".dirhidden"
    ]
}

predicted_lists_recursive = {
    "R": {
        "": [ "dir0", "dir1", "dir2", "file0" ],
        "dir0": [],
        "dir1": [ "dir1_A", "dir1_file0" ],
        "dir1/dir1_A": [],
        "dir2": [ "dir2_A", "dir2_B" ],
        "dir2/dir2_A": [ "dir2_A_file0", "dir2_A_file1" ],
        "dir2/dir2_B": [ "dir2_B_filebig" ]
    },
    "Ra": {
        "": [ ".dirhidden", "dir0", "dir1", "dir2", "file0" ],
        ".dirhidden": [ ".dirhidden_filehidden" ],
        "dir0": [],
        "dir1": [ "dir1_A", ".dir1_filehidden", "dir1_file0" ],
        "dir1/dir1_A": [],
        "dir2": [ "dir2_A", "dir2_B" ],
        "dir2/dir2_A": [ "dir2_A_file0", "dir2_A_file1" ],
        "dir2/dir2_B": [ "dir2_B_filebig" ]
    },
    "Rr": {
        "": [ "dir2", "dir1", "dir0", "file0" ],
        "dir2": [ "dir2_B", "dir2_A" ],
        "dir2/dir2_B": [ "dir2_B_filebig" ],
        "dir2/dir2_A": [ "dir2_A_file1", "dir2_A_file0" ],
        "dir1": [ "dir1_A", "dir1_file0" ],
        "dir1/dir1_A": [],
        "dir0": []
    },
    "Rar": {
        "": [ "dir2", "dir1", "dir0", ".dirhidden", "file0" ],
        "dir2": [ "dir2_B", "dir2_A" ],
        "dir2/dir2_B": [ "dir2_B_filebig" ],
        "dir2/dir2_A": [ "dir2_A_file1", "dir2_A_file0" ],
        "dir1": [ "dir1_A", "dir1_file0", ".dir1_filehidden" ],
        "dir1/dir1_A": [],
        "dir0": [],
        ".dirhidden": [ ".dirhidden_filehidden" ]
    }
}

predicted_lists_recursive_directories = {
    "Rd": {
        "": [ "dir0", "dir1", "dir2" ],
        "dir0": [],
        "dir1": [ "dir1_A" ],
        "dir1/dir1_A": [],
        "dir2": [ "dir2_A", "dir2_B" ],
        "dir2/dir2_A": [],
        "dir2/dir2_B": []
    },
    "Rrd": {
        "": [ "dir2", "dir1", "dir0" ],
        "dir2": [ "dir2_B", "dir2_A" ],
        "dir2/dir2_B": [],
        "dir2/dir2_A": [],
        "dir1": [ "dir1_A" ],
        "dir1/dir1_A": [],
        "dir0": []
    },
    "Rad": {
        "": [ ".dirhidden", "dir0", "dir1", "dir2" ],
        ".dirhidden": [],
        "dir0": [],
        "dir1": [ "dir1_A" ],
        "dir1/dir1_A": [],
        "dir2": [ "dir2_A", "dir2_B" ],
        "dir2/dir2_A": [],
        "dir2/dir2_B": []
    },
    "Rard": {
        "": [ "dir2", "dir1", "dir0", ".dirhidden" ],
        "dir2": [ "dir2_B", "dir2_A" ],
        "dir2/dir2_B": [],
        "dir2/dir2_A": [],
        "dir1": [ "dir1_A" ],
        "dir1/dir1_A": [],
        "dir0": [],
        ".dirhidden": []
    }
}
