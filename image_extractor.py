'''
Created on Nov 1, 2022

@author: loganoscher
'''

def main():
    import instaloader
    test = instaloader.Instaloader()
    acc = input('Enter the Account Username: ')
    test.download_profile(acc, profile_pic=True, profile_pic_only=False, fast_update=False, download_stories=False, download_stories_only=False, download_tagged=False, download_tagged_only=False, post_filter=None, storyitem_filter=None)     

if __name__ == '__main__':
    main()
