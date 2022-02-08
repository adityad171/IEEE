HTMLString = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <link
            href="https://fonts.googleapis.com/icon?family=Material+Icons"
            rel="stylesheet"
        />
        <link rel="stylesheet" href="../dist/output.css" />
        <title>IEEE IIITD Member - Jack</title>
    </head>
    <body class="flex flex-col md:min-h-screen">
        <!-- header -->
        <header class="header">
            <nav class="nav">
                <div class="container mx-auto my-5">
                    <div
                        class="flex justify-between items-center px-4 md:px-0 py-2"
                    >
                        <div class="flex items-center">
                            <a href="index.html">
                                <img
                                    src="../assets/index/logo.png"
                                    alt="logo"
                                    class="h-12"
                                />
                            </a>
                        </div>
                        <div class="flex items-center">
                            <a href="../events.html" class="heading2 px-4 py-2"
                                >events</a
                            >
                            <a href="../members.html" class="heading2 px-4 py-2"
                                >members</a
                            >
                            <a
                                href="#contact"
                                class="heading2 px-4 md:px-0 md:pl-4 py-2"
                                >contact</a
                            >
                        </div>
                    </div>
                </div>
            </nav>
        </header>

        <!-- main -->
        <main class="flex-auto">
            <!-- details -->
            <section id="details" class="md:min-h-screen">
                <div class="container mx-auto mt-40">
                    <div class="flex flex-col">
                        <div class="flex flex-col md:flex-row justify-around">
                            <div class="memPgImg flex flex-col">
                                <h3 class="text-sm text-gray-500 font-semibold">members / {sname}</h6>
                                <br />
                                <img src="{img}" alt="{aname}" class="rounded-xl" />
                                <br><br>
                                <div class="flex flex-row justify-between">
                                    <img src="https://via.placeholder.com/50x50" alt="" class="rounded-full"/>
                                    <img src="https://via.placeholder.com/50x50" alt="" class="rounded-full"/>
                                    <img src="https://via.placeholder.com/50x50" alt="" class="rounded-full"/>
                                </div>
                            </div>
                            <div class="memPgTxt flex flex-col w-32 space-y-5">
                                <br>
                                <h1 class="heading text-5xl">{name}</h1>
                                <h2 class="text-3xl font-semibold text-gray-500">{pos}</h2>
                                <p class="text-gray-500 leading-10">
                                    {desc}
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- contact -->
            <section id="contact" class="footer-bg">
                <div class="container mx-auto">
                    <div
                        class="flex flex-col md:flex-row text-white py-20 justify-between md:ml-10 w-full space-y-5"
                    >
                        <a href="">
                            <div
                                class="memAlum flex flex-col p-7 justify-end items-end text-right rounded-xl"
                            >
                                <h1 class="heading text-3xl font-bold">
                                    Our Members and Alumni
                                </h1>
                                <br />
                                <div
                                    class="rounded-full border-1 py-2 px-2 flex justify-center items-center"
                                    style="background: #f8f8f870"
                                >
                                    <i class="material-icons text-white">
                                        keyboard_arrow_right
                                    </i>
                                </div>
                            </div>
                        </a>
                        <div class="flex flex-col">
                            <h1
                                class="fancyJoin heading text-2xl md:text-4xl font-bold leading-10"
                            >
                                Join Us.
                            </h1>
                            <br />
                            <h2
                                class="heading text-2xl md:text-4xl font-bold w-full md:w-1/2"
                            >
                                Become a part of the exclusive community.
                            </h2>
                            <br /><br />
                            <h3 class="font-bold">Perks</h3>
                            <ul class="text-gray-500">
                                <li>
                                    Lorem ipsum dolor sit amet consectetur
                                    adipisicing elit.
                                </li>
                                <li>
                                    Lorem ipsum dolor sit amet consectetur
                                    adipisicing elit.
                                </li>
                                <li>
                                    Lorem ipsum dolor sit amet consectetur
                                    adipisicing elit.
                                </li>
                            </ul>
                            <br /><br />
                            <a href="">
                                <button
                                    class="heading2 applyBtn bg-white px-10 py-2 text-black rounded-lg"
                                >
                                    apply
                                </button>
                            </a>
                        </div>
                    </div>
                    <hr class="border-gray-500 rounded-full mx-auto" />
                </div>
            </section>
        </main>

        <!-- footer -->
        <footer class="footer-bg px-8">
            <div class="container mx-auto my-14 mb-28">
                <div
                    class="flex flex-col md:flex-row md:justify-between text-white md:mx-auto space-y-5 md:space-y-5"
                >
                    <div
                        class="flex flex-col md:flex-row space-y-5 md:space-y-0 md:space-x-5 w-full md:w-1/4 md:mx-auto"
                    >
                        <div class="flex pt-4 text-white">
                            <img
                                src="../assets/index/logowhite.png"
                                alt="logo"
                                class="footerLogo"
                            />
                        </div>
                        <div class="flex flex-col md:justify-center">
                            <h1 class="heading text-xl font-bold">IEEE</h1>
                            <h1 class="heading text-xl font-bold">
                                IIIT Delhi
                            </h1>
                            <h2 class="heading text-md font-bold text-gray-500">
                                student branch
                            </h2>
                            <br />
                            <p class="text-sm text-gray-500">
                                IIIT Delhi, Okhla Industrial, <br />
                                Phase-III, New Delhi-110020
                            </p>
                        </div>
                    </div>
                    <div
                        class="flex flex-col md:flex-row md:justify-between w-full md:w-1/3 md:mx-auto"
                    >
                        <div
                            class="flex flex-col w-full md:w-1/2 md:mx-16 mb-5 md:mb-5"
                        >
                            <h1 class="heading font-bold">Affiliations</h1>
                            <div
                                class="flex flex-wrap md:flex-col space-x-5 md:space-x-0"
                            >
                                <a href="" class="text-gray-500">IIIT Delhi</a>
                                <a href="" class="text-gray-500">IEEE</a>
                                <a href="" class="text-gray-500">WiE</a>
                                <a href="" class="text-gray-500">CompSoc</a>
                            </div>
                        </div>
                        <div class="flex flex-col w-full md:w-1/2 md:mx-16">
                            <h1 class="heading font-bold">Socials</h1>
                            <div
                                class="flex flex-wrap md:flex-col md:space-x-0"
                            >
                                <a href="" class="pr-5 md:pr-0 text-gray-500"
                                    >Instagram</a
                                >
                                <a href="" class="pr-5 md:pr-0 text-gray-500"
                                    >Facebook</a
                                >
                                <a href="" class="pr-5 md:pr-0 text-gray-500"
                                    >LinkedIn</a
                                >
                                <a href="" class="pr-5 md:pr-0 text-gray-500"
                                    >YouTube</a
                                >
                                <a href="" class="pr-5 md:pr-0 text-gray-500"
                                    >Twitter</a
                                >
                            </div>
                        </div>
                    </div>
                    <div class="flex flex-col w-full md:w-1/5 md:ml-16">
                        <h1 class="heading font-bold">Contact</h1>
                        <p class="text-gray-500">
                            <a href="mailto:ieee@iiitd.ac.in"
                                >ieee@iiitd.ac.in</a
                            >
                        </p>
                        <br />
                        <h1 class="heading font-bold">Graphic Identity</h1>
                    </div>
                </div>
            </div>
        </footer>
    </body>
</html>
"""

data = {
    0: {
        "name": "Prof. S. S. Jamuar",
        "pos": "Faculty Coordinator",
        "img": "https://via.placeholder.com/100x100",
        "social": {
            "fb": "https://www.facebook.com/",
            "tw": "https://twitter.com/",
            "wb": "#"
        },
        "desc": "lorem"
    },
    1: {
        "name": "Dr. Shobha Sundar Ram",
        "pos": "Head of Department, ECE",
        "img": "https://via.placeholder.com/100x100",
        "social": {
            "fb": "https://www.facebook.com/",
            "tw": "https://twitter.com/",
            "wb": "#"
        },
        "desc": "lorem"
    },
    2: {
        "name": "Dr. Rajiv Ratn Shah",
        "pos": "CompSoc Faculty Coordinator",
        "img": "https://via.placeholder.com/100x100",
        "social": {
            "fb": "https://www.facebook.com/",
            "tw": "https://twitter.com/",
            "wb": "#"
        },
        "desc": "lorem"
    },
    3: {
        "name": "Prakhar Prasad",
        "pos": "Chairperson",
        "img": "https://via.placeholder.com/100x100",
        "social": {
            "fb": "https://www.facebook.com/",
            "tw": "https://twitter.com/",
            "wb": "#"
        },
        "desc": "lorem"
    },
    4: {
        "name": "Ansh Arora",
        "pos": "Vice Chairperson",
        "img": "https://via.placeholder.com/100x100",
        "social": {
            "fb": "https://www.facebook.com/",
            "tw": "https://twitter.com/",
            "wb": "#"
        },
        "desc": "lorem"
    },
    5: {
        "name": "Gursimran Kaur",
        "pos": "Secretary / Coordinator",
        "img": "https://via.placeholder.com/100x100",
        "social": {
            "fb": "https://www.facebook.com/",
            "tw": "https://twitter.com/",
            "wb": "#"
        },
        "desc": "lorem"
    },
    6: {
        "name": "Garmit Pant",
        "pos": "Treasurer / Coordinator",
        "img": "https://via.placeholder.com/100x100",
        "social": {
            "fb": "https://www.facebook.com/",
            "tw": "https://twitter.com/",
            "wb": "#"
        },
        "desc": "lorem"
    },
    7: {
        "name": "Mihir Chaturvedi",
        "pos": "WebMaster",
        "img": "https://via.placeholder.com/100x100",
        "social": {
            "fb": "https://www.facebook.com/",
            "tw": "https://twitter.com/",
            "wb": "#"
        },
        "desc": "lorem"
    },
    8: {
        "name": "Daksh T",
        "pos": "Industrial Outreach",
        "img": "https://via.placeholder.com/100x100",
        "social": {
            "fb": "https://www.facebook.com/",
            "tw": "https://twitter.com/",
            "wb": "#"
        },
        "desc": "lorem"
    },
    9: {
        "name": "Sachleen Kaur",
        "pos": "Design Head",
        "img": "https://via.placeholder.com/100x100",
        "social": {
            "fb": "https://www.facebook.com/",
            "tw": "https://twitter.com/",
            "wb": "#"
        },
        "desc": "lorem"
    },
    10: {
        "name": "Shragvi Sidarth Jha",
        "pos": "Operations Head",
        "img": "https://via.placeholder.com/100x100",
        "social": {
            "fb": "https://www.facebook.com/",
            "tw": "https://twitter.com/",
            "wb": "#"
        },
        "desc": "lorem"
    },
    11: {
        "name": "Niranjan Sundarajan",
        "pos": "Events Head",
        "img": "https://via.placeholder.com/100x100",
        "social": {
            "fb": "https://www.facebook.com/",
            "tw": "https://twitter.com/",
            "wb": "#"
        },
        "desc": "lorem"
    },
    12: {
        "name": "Meetakshi Setiya",
        "pos": "WiE Chairperson / Coordinator",
        "img": "https://via.placeholder.com/100x100",
        "social": {
            "fb": "https://www.facebook.com/",
            "tw": "https://twitter.com/",
            "wb": "#"
        },
        "desc": "lorem"
    },
    13: {
        "name": "Amolika Bansal",
        "pos": "Vice Chairperson",
        "img": "https://via.placeholder.com/100x100",
        "social": {
            "fb": "https://www.facebook.com/",
            "tw": "https://twitter.com/",
            "wb": "#"
        },
        "desc": "lorem"
    },
    14: {
        "name": "Sunishka Sharma",
        "pos": "Secretary",
        "img": "https://via.placeholder.com/100x100",
        "social": {
            "fb": "https://www.facebook.com/",
            "tw": "https://twitter.com/",
            "wb": "#"
        },
        "desc": "lorem"
    },
    15: {
        "name": "Rohan Dhar",
        "pos": "CompSoc Chairperson",
        "img": "https://via.placeholder.com/100x100",
        "social": {
            "fb": "https://www.facebook.com/",
            "tw": "https://twitter.com/",
            "wb": "#"
        },
        "desc": "lorem"
    },
    16: {
        "name": "Abhik S Basu",
        "pos": "Vice Chairperson",
        "img": "https://via.placeholder.com/100x100",
        "social": {
            "fb": "https://www.facebook.com/",
            "tw": "https://twitter.com/",
            "wb": "#"
        },
        "desc": "lorem"
    },
    17: {
        "name": "Raghav Sahni",
        "pos": "ExeCom",
        "img": "https://via.placeholder.com/100x100",
        "social": {
            "fb": "https://www.facebook.com/",
            "tw": "https://twitter.com/",
            "wb": "#"
        },
        "desc": "lorem"
    },
    18: {
        "name": "Tejdeep Ch",
        "pos": "ExeCom",
        "img": "https://via.placeholder.com/100x100",
        "social": {
            "fb": "https://www.facebook.com/",
            "tw": "https://twitter.com/",
            "wb": "#"
        },
        "desc": "lorem"
    },
    19: {
        "name": "Anusha Tiwari",
        "pos": "ExeCom",
        "img": "https://via.placeholder.com/100x100",
        "social": {
            "fb": "https://www.facebook.com/",
            "tw": "https://twitter.com/",
            "wb": "#"
        },
        "desc": "lorem"
    },
    20: {
        "name": "Ritwick Pal",
        "pos": "ExeCom",
        "img": "https://via.placeholder.com/100x100",
        "social": {
            "fb": "https://www.facebook.com/",
            "tw": "https://twitter.com/",
            "wb": "#"
        },
        "desc": "lorem"
    },
    21: {
        "name": "Jogith S Chandran",
        "pos": "ExeCom",
        "img": "https://via.placeholder.com/100x100",
        "social": {
            "fb": "https://www.facebook.com/",
            "tw": "https://twitter.com/",
            "wb": "#"
        },
        "desc": "lorem"
    },
    22: {
        "name": "Samyak Jain",
        "pos": "ExeCom",
        "img": "https://via.placeholder.com/100x100",
        "social": {
            "fb": "https://www.facebook.com/",
            "tw": "https://twitter.com/",
            "wb": "#"
        },
        "desc": "lorem"
    },
    23: {
        "name": "Mohit Jain",
        "pos": "ExeCom",
        "img": "https://via.placeholder.com/100x100",
        "social": {
            "fb": "https://www.facebook.com/",
            "tw": "https://twitter.com/",
            "wb": "#"
        },
        "desc": "lorem"
    },
    24: {
        "name": "Aayush Kapoor",
        "pos": "ExeCom",
        "img": "https://via.placeholder.com/100x100",
        "social": {
            "fb": "https://www.facebook.com/",
            "tw": "https://twitter.com/",
            "wb": "#"
        },
        "desc": "lorem"
    },
    25: {
        "name": "Max",
        "pos": "CMO",
        "img": "https://via.placeholder.com/100x100",
        "social": {
            "fb": "https://www.facebook.com/",
            "tw": "https://twitter.com/",
            "wb": "#"
        },
        "desc": "lorem"
    },
    26: {
        "name": "Jack",
        "pos": "CO",
        "img": "https://via.placeholder.com/100x100",
        "social": {
            "fb": "https://www.facebook.com/",
            "tw": "https://twitter.com/",
            "wb": "#"
        },
        "desc": "lorem"
    }
}

BASE_DIR = "./members/"

print("PROCESS STARTED")
print("PROCESSING ...")
# print(HTMLString.format(name = data[26]["name"]), pos = data[26]["pos"], img = data[26]["img"], desc = data[26]["desc"])
for i in range(len(data)):
    f = open(BASE_DIR + str(i+1) + ".html", "w")
    sname = data[i]["name"]
    img = data[i]["img"]
    aname = data[i]["name"]
    name = data[i]["name"]
    pos = data[i]["pos"]
    desc = data[i]["desc"]
    f.write(HTMLString.format(sname = sname, aname = aname, name = name, pos = pos, img = img, desc = desc))
    f.close()
print("PROCESS COMPLETED")