import redis
import geojson as gj

def test_tile38():
    client = redis.Redis(host='127.0.0.1', port=9851)
    # insert data
    for p in _get_points():
        client.execute_command('SET', 'fleet', 'v', 'FIELD', 'timestamp',  str(p['timestamp']),
        'POINT', p['coords'][0], p['coords'][1], int(p['timestamp']))

    # get data
    #print(client.execute_command('GET', 'fleet', 'v'))

def _get_points():
    with open('data/geojson/path_points_4326.geojson') as f:
        gjf = gj.load(f)
    feature_collection = gjf['features']
    points = []
    for ftr in feature_collection:
        p = {
                'id': ftr['properties']['id'],
                'coords': (ftr['geometry']['coordinates'][1], ftr['geometry']['coordinates'][0]),  # (lat,lon)
                'timestamp': ftr['properties']['timestamp']
        }
        points.append(p)
    return points

if __name__ == '__main__':
    test_tile38()