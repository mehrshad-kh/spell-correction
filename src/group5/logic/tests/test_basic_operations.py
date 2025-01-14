import pytest

from src.group5.logic.miss_spell_finder import BasicOperations



class TestBasicOperations:

    def setup_method(self, method):
        self.basic_ops = BasicOperations([], 0)

    @pytest.mark.parametrize("word", ["سلام"])
    def test_deletion(self, word):
        assert self.basic_ops.deletion(word) == ['لام', 'سام', 'سلم', 'سلا']

    @pytest.mark.parametrize("word", ["سلام"])
    def test_insertion(self, word):
        assert self.basic_ops.insertion(word) == ['اسلام', 'آسلام', 'بسلام', 'پسلام', 'تسلام', 'ثسلام', 'جسلام',
                                                  'چسلام', 'حسلام', 'خسلام', 'دسلام', 'ذسلام', 'رسلام', 'زسلام',
                                                  'ژسلام', 'سسلام', 'شسلام', 'صسلام', 'ضسلام', 'طسلام', 'ظسلام',
                                                  'عسلام', 'غسلام', 'فسلام', 'قسلام', 'کسلام', 'گسلام', 'لسلام',
                                                  'مسلام', 'نسلام', 'وسلام', 'هسلام', 'یسلام', '\u200cسلام', 'سالام',
                                                  'سآلام', 'سبلام', 'سپلام', 'ستلام', 'سثلام', 'سجلام', 'سچلام',
                                                  'سحلام', 'سخلام', 'سدلام', 'سذلام', 'سرلام', 'سزلام', 'سژلام',
                                                  'سسلام', 'سشلام', 'سصلام', 'سضلام', 'سطلام', 'سظلام', 'سعلام',
                                                  'سغلام', 'سفلام', 'سقلام', 'سکلام', 'سگلام', 'سللام', 'سملام',
                                                  'سنلام', 'سولام', 'سهلام', 'سیلام', 'س\u200cلام', 'سلاام', 'سلآام',
                                                  'سلبام', 'سلپام', 'سلتام', 'سلثام', 'سلجام', 'سلچام', 'سلحام',
                                                  'سلخام', 'سلدام', 'سلذام', 'سلرام', 'سلزام', 'سلژام', 'سلسام',
                                                  'سلشام', 'سلصام', 'سلضام', 'سلطام', 'سلظام', 'سلعام', 'سلغام',
                                                  'سلفام', 'سلقام', 'سلکام', 'سلگام', 'سللام', 'سلمام', 'سلنام',
                                                  'سلوام', 'سلهام', 'سلیام', 'سل\u200cام', 'سلاام', 'سلاآم', 'سلابم',
                                                  'سلاپم', 'سلاتم', 'سلاثم', 'سلاجم', 'سلاچم', 'سلاحم', 'سلاخم',
                                                  'سلادم', 'سلاذم', 'سلارم', 'سلازم', 'سلاژم', 'سلاسم', 'سلاشم',
                                                  'سلاصم', 'سلاضم', 'سلاطم', 'سلاظم', 'سلاعم', 'سلاغم', 'سلافم',
                                                  'سلاقم', 'سلاکم', 'سلاگم', 'سلالم', 'سلامم', 'سلانم', 'سلاوم',
                                                  'سلاهم', 'سلایم', 'سلا\u200cم', 'سلاما', 'سلامآ', 'سلامب', 'سلامپ',
                                                  'سلامت', 'سلامث', 'سلامج', 'سلامچ', 'سلامح', 'سلامخ', 'سلامد',
                                                  'سلامذ', 'سلامر', 'سلامز', 'سلامژ', 'سلامس', 'سلامش', 'سلامص',
                                                  'سلامض', 'سلامط', 'سلامظ', 'سلامع', 'سلامغ', 'سلامف', 'سلامق',
                                                  'سلامک', 'سلامگ', 'سلامل', 'سلامم', 'سلامن', 'سلامو', 'سلامه',
                                                  'سلامی', 'سلام\u200c']

    @pytest.mark.parametrize("word", ["سلام"])
    def test_substitution(self, word):
        assert self.basic_ops.substitution(word) == ['الام', 'آلام', 'بلام', 'پلام', 'تلام', 'ثلام', 'جلام', 'چلام',
                                                     'حلام', 'خلام', 'دلام', 'ذلام', 'رلام', 'زلام', 'ژلام', 'سلام',
                                                     'شلام', 'صلام', 'ضلام', 'طلام', 'ظلام', 'علام', 'غلام', 'فلام',
                                                     'قلام', 'کلام', 'گلام', 'للام', 'ملام', 'نلام', 'ولام', 'هلام',
                                                     'یلام', '\u200cلام', 'ساام', 'سآام', 'سبام', 'سپام', 'ستام',
                                                     'سثام', 'سجام', 'سچام', 'سحام', 'سخام', 'سدام', 'سذام', 'سرام',
                                                     'سزام', 'سژام', 'سسام', 'سشام', 'سصام', 'سضام', 'سطام', 'سظام',
                                                     'سعام', 'سغام', 'سفام', 'سقام', 'سکام', 'سگام', 'سلام', 'سمام',
                                                     'سنام', 'سوام', 'سهام', 'سیام', 'س\u200cام', 'سلام', 'سلآم',
                                                     'سلبم', 'سلپم', 'سلتم', 'سلثم', 'سلجم', 'سلچم', 'سلحم', 'سلخم',
                                                     'سلدم', 'سلذم', 'سلرم', 'سلزم', 'سلژم', 'سلسم', 'سلشم', 'سلصم',
                                                     'سلضم', 'سلطم', 'سلظم', 'سلعم', 'سلغم', 'سلفم', 'سلقم', 'سلکم',
                                                     'سلگم', 'سللم', 'سلمم', 'سلنم', 'سلوم', 'سلهم', 'سلیم',
                                                     'سل\u200cم', 'سلاا', 'سلاآ', 'سلاب', 'سلاپ', 'سلات', 'سلاث',
                                                     'سلاج', 'سلاچ', 'سلاح', 'سلاخ', 'سلاد', 'سلاذ', 'سلار', 'سلاز',
                                                     'سلاژ', 'سلاس', 'سلاش', 'سلاص', 'سلاض', 'سلاط', 'سلاظ', 'سلاع',
                                                     'سلاغ', 'سلاف', 'سلاق', 'سلاک', 'سلاگ', 'سلال', 'سلام', 'سلان',
                                                     'سلاو', 'سلاه', 'سلای', 'سلا\u200c']

    @pytest.mark.parametrize("word, output", [("سلام", ['لسام', 'سالم', 'سلما'])])
    def test_transposition(self, word, output):
        assert self.basic_ops.transposition(word) == output

