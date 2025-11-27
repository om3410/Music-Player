from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from .models import Song

def index(request):
    """Main music player view"""
    songs = Song.objects.all()
    
    # Pagination for the first template approach
    paginator = Paginator(songs, 1)  # Show 1 song per page
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'App/index.html', {
        'songs': songs,
        'page_obj': page_obj,
    })

@csrf_exempt
def songs_api(request):
    """API endpoint to return songs as JSON for frontend JavaScript"""
    if request.method == 'GET':
        songs = Song.objects.all()
        
        songs_data = []
        for song in songs:
            song_data = {
                'id': song.id,
                'title': song.title,
                'artist': song.artist,
                'audio_file': song.get_audio_url(),  # Fixed: Added parentheses
                'audio_link': song.audio_link or '',
                'image': song.get_image_url() or '/static/images/default-cover.jpg',  # Fixed: Added default fallback
                'lyrics': song.lyrics or 'No lyrics available',
                'duration': song.duration,
            }
            songs_data.append(song_data)
        
        return JsonResponse(songs_data, safe=False)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)