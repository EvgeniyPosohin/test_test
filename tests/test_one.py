import pytest
from dz import*



@pytest.mark.parametrize(
    'mentors, expected', [
        [mentors, [['Александр', 10], ['Евгений', 5], ['Максим', 4]]]])
def test_get_unique_names(mentors, expected):
    result = uniqe_name(mentors)
    assert result == expected

@pytest.mark.parametrize('mentors', [mentors])
def test_1(mentors):
    res = search_name(mentors)[:3]
    expected = ['Адилет', 'Азамат', 'Александр']
    assert res == expected

@pytest.mark.parametrize(
    'mentors, durations,', [
        [mentors, [14, 20, 12, 20]]])
def test_get_unique_names(mentors, durations):
    result = super_name(mentors, courses, durations)
    expected = {'short_courses': [['Fullstack-разработчик на Python'], 12],
                'long_courses': [['Java-разработчик с нуля', 'Frontend-разработчик с нуля'], 20]}
    assert result == expected
