from django.shortcuts import render

people = [
    {
        "name": "Albert Einstein",
        "profession": "Physicist",
        "short_info": "Creator of the theory of relativity.",
        "full_info": "Albert Einstein was the founder of the theory of relativity. He received the Nobel Prize in 1921 for his explanation of the photoelectric effect.",
        "image": "images/einstein.jpg"
    },
    {
        "name": "Marie Curie",
        "profession": "Chemist and Physicist",
        "short_info": "Pioneer in radioactivity research and Nobel Prize winner.",
        "full_info": "Marie Curie was the first scientist to work extensively on radioactivity. She remains the only person awarded Nobel Prizes in two different sciences.",
        "image": "images/curie.jpg"
    },
    {
        "name": "Leonardo da Vinci",
        "profession": "Painter and Inventor",
        "short_info": "Mastermind behind the Mona Lisa and The Last Supper.",
        "full_info": "Leonardo da Vinci was a genius of the Renaissance. He made lasting contributions in painting, architecture, science, and engineering.",
        "image": "images/davinci.jpg"
    }
]

def index(request):
    return render(request, 'index.html', {'people': people})

def person_list(request):
    return render(request, 'index.html', {'people': people})

def person_detail(request, person_id):
    return render(request, 'person_detail.html', {'person': people[person_id-1]})
