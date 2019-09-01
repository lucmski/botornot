package cmd

import (
	"fmt"
	"os"
	"time"

	"github.com/ChimeraCoder/anaconda"
	//	"github.com/fatih/structs"
	"github.com/k0kubun/pp"
	"github.com/lucmski/botornot/pkg/config"
	"github.com/spf13/cobra"
)

var options config.Options

// RootCmd is the root command
var RootCmd = &cobra.Command{
	Use:     "botornot",
	Short:   "botornot",
	Long:    `botornot.`,
	Version: config.Version,
	Run: func(cmd *cobra.Command, args []string) {
		pp.Println("hello botornot !")
		api := anaconda.NewTwitterApiWithCredentials(
			"435770893-poT6l1c4v9ucWCrtonn1rXy0KCc3wJjv7OaztX7D",
			"TKMUSR9xRL5GndHm1WYAq8Wyedai5PTkQsBPFPL2iFo2q",
			"qvXuwN9IrYAEaroxyTE0d7cQS",
			"M6lIVHX3FqyOKZmi37tCfSIWNyRaLruqakcA1MFoEejHGZFXFI",
		)
		pp.Println(*api.Credentials)
		ExampleTwitterApi_Throttling(api)

		/*
			pages := api.GetFollowersListAll(nil)
			pp.Println(len(pages))
			for page := range pages {
				//Print the current page of followers
				pp.Println(page.Followers)
				// pp.Println(structs.Map(page.Followers))
				// for follower := range page.Followers {
				//	pp.Println(follower)
				// }
			}
		*/
	},
}

// Execute adds all child commands to the root command and sets flags appropriately.
func Execute() {
	if err := RootCmd.Execute(); err != nil {
		fmt.Println(err)
		os.Exit(-1)
	}
}

func init() {
	flags := RootCmd.PersistentFlags()
	flags.BoolVarP(&options.NoColor, "no-color", "n", false, "no color")
	flags.BoolVarP(&options.CheckForUpdate, "update", "u", false, "check for updates")
	flags.BoolVarP(&options.Verbose, "verbose", "v", false, "verbose output")
}

func ExampleTwitterApi_GetSearch() {
	anaconda.SetConsumerKey("your-consumer-key")
	anaconda.SetConsumerSecret("your-consumer-secret")
	api := anaconda.NewTwitterApi("your-access-token", "your-access-token-secret")
	search_result, err := api.GetSearch("golang", nil)
	if err != nil {
		panic(err)
	}
	for _, tweet := range search_result.Statuses {
		fmt.Print(tweet.Text)
	}
}

// Throttling queries can easily be handled in the background, automatically
func ExampleTwitterApi_Throttling(api *anaconda.TwitterApi) {
	// api := anaconda.NewTwitterApi("your-access-token", "your-access-token-secret")
	api.EnableThrottling(10*time.Second, 5)

	// These queries will execute in order
	// with appropriate delays inserted only if necessary
	golangTweets, err := api.GetSearch("golang", nil)
	anacondaTweets, err2 := api.GetSearch("anaconda", nil)

	if err != nil {
		panic(err)
	}
	if err2 != nil {
		panic(err)
	}

	fmt.Println(golangTweets)
	fmt.Println(anacondaTweets)
}
