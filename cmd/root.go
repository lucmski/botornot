package cmd

import (
	"fmt"
	"os"

	"github.com/k0kubun/pp"
	"github.com/lucmski/botornot/pkg/config"
	"github.com/spf13/cobra"
)

var options config.Options

// RootCmd is the root command
var RootCmd = &cobra.Command{
	Use:     "investigo",
	Short:   "investigos",
	Long:    `investigo.`,
	Version: config.Version,
	Run: func(cmd *cobra.Command, args []string) {
		pp.Println("hello !")
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
