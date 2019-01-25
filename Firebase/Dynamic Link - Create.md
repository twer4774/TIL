# Dynamic Link

출처: https://github.com/distriqt/ANE-Firebase/wiki/DynamicLinks---Create-Dynamic-Links

## Create Dynmic Links

- 생성방법은 총 4가지
  1. 콘솔창을 이용해 만드는 방법. 1회용 링크를 만드는 경우 유용
  2. Dynamic Link Builder API 이용. 사용자 간 공유 또는 많은 링크가 필요한 상황에서 앱의 링크를 동적으로 생성하는 기본 방법
  3. REST API 이용. 플랫폼에서 동적으로 링크를 작성하는 기본 방법
  4. 직접 만들기. Firebase 콘솔에서 <u>클릭 데이터를 추적할 필요가 없고</u>, 길이가 긴 URL이여도 상관없다면 이용. 네트워크 왕복을 피할 수 있는 장점이 있음

### Builder API 사용

- 짧거나 긴 동적 링크를 만듦

- 동적 링크 매개변수를 포함하는 객체를 받아들이고 아래와 같은 URL 반환

  ```s
  https://abc123.app.goo.gl/WXYZ
  ```

- 매개 변수로 동적 링크 만들기

  - 긴 Dynamic Link

  ```
  var builder:DynamicLinkBuilder = new DynamicLinkBuilder()
  		.setLink( "https://example.com" )
  		.setDynamicLinkDomain( "abc123.app.goo.gl" )
  		.setAndroidParameters( new AndroidParametersBuilder().build() )
  		.setIosParameters( new IosParametersBuilder( "com.example.ios" ).build() );
  
  var link:DynamicLink = FirebaseDynamicLinks.service.createDynamicLink( builder.build() );
  ```

  - 짧은 Dynamic Link
    - 짧은 Dynamic Link를 만들려면 네트워크 호출이 필요함
    - `ShortDynamicLinkEvent.LINK_CREATED` : 짧은 링크가 생성 된 경우 전달됩니다.
    - `ShortDynamicLinkEvent.ERROR` : 짧은 링크를 생성하는 중에 오류가 발생하면 전달됩니다.

- ```
  FirebaseDynamicLinks.service.addEventListener( ShortDynamicLinkEvent.LINK_CREATED, dynamicLinkCreatedHandler );
  FirebaseDynamicLinks.service.addEventListener( ShortDynamicLinkEvent.ERROR, dynamicLinkErrorHandler );
  
  var builder:DynamicLinkBuilder = new DynamicLinkBuilder()
  		.setLink( "https://example.com" )
  		.setDynamicLinkDomain( "abc123.app.goo.gl" )
  		.setAndroidParameters( new AndroidParametersBuilder().build() )
  		.setIosParameters( new IosParametersBuilder( "com.example.ios" ).build() );
  
  FirebaseDynamicLinks.service.createShortDynamicLink( builder.build() );
  ```

  - 짧은 Dynamic Link응답

  ```
  function dynamicLinkCreatedHandler( event:ShortDynamicLinkEvent ):void
  {
  	trace( "dynamicLinkCreatedHandler() : " + event.link.shortLink );
  }
  
  function dynamicLinkErrorHandler( event:ShortDynamicLinkEvent ):void
  {
  	trace( "dynamicLinkErrorHandler()" );
  }
  ```

- Dynamic Link parameters

  - 동적 링크에 설정할 수 있는 매개변수의 범위
  - 이를 이용하면 좀 더 나은 동적링크를 생성할 수 있음

  ```
  var link:DynamicLink = FirebaseDynamicLinks.service.createDynamicLink(
  		new DynamicLinkBuilder()
  				.setLink( "https://airnativeextensions.com" )
  				.setDynamicLinkDomain( "bb9g6.app.goo.gl" )
  				.setAndroidParameters(
  						new AndroidParametersBuilder( "air.com.distriqt.test" )
  								.setFallbackUrl("https://airnativeextensions.com")
  								.build()
  				)
  				.setIosParameters(
  						new IosParametersBuilder( "com.distriqt.test" )
  								.setFallbackUrl("https://airnativeextensions.com")
  								.build()
  				)
  				.setGoogleAnalyticsParameters(
  						new GoogleAnalyticsParametersBuilder()
  								.setSource("orkut")
  								.setMedium("social")
  								.setCampaign("example-promo")
  								.build()
  				)
  				.setItunesConnectAnalyticsParameters(
  						new ItunesConnectAnalyticsParametersBuilder()
  								.setProviderToken( "123456" )
  								.setCampaignToken("example-promo")
  								.build()
  				)
  				.setSocialMetaTagParameters(
  						new SocialMetaTagParametersBuilder()
  								.setTitle("Example of a Dynamic Link")
  								.setDescription("This link works whether the app is installed or not!")
  								.build()
  				)
  				.build()
  );
  ```
